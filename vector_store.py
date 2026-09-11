# vector_store.py
from pathlib import Path
import atexit

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,   
    MatchAny,
    Filter,
    FieldCondition,
    MatchValue,
    FilterSelector,
    PointStruct
)
from uuid import uuid5, NAMESPACE_URL

from models import IndexedChunk, RetrievalFilter, VectorSearchResult

COLLECTION_NAME = "infrastructure_knowledge"
VECTOR_SIZE = 1536

client = QdrantClient(path="qdrant_data")
atexit.register(client.close)

def initialize_collection() -> None:
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

EMBEDDINGS_FILE = Path("embeddings.json")

def save_chunks(
    chunks: dict[str, IndexedChunk],
) -> None:
    initialize_collection()
    points: list[PointStruct] = []

    for chunk in chunks.values():
        point_id = str(
            uuid5(
                NAMESPACE_URL,
                chunk.chunk_id,
            )
        )

        points.append(
            PointStruct(
                id=point_id,
                vector=chunk.embedding,
                payload={
                    "chunk_id": chunk.chunk_id,
                    "source": chunk.source,
                    "text": chunk.text,
                    "modified_at": chunk.modified_at,
                },
            )
        )

    if points:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
            wait=True,
        )

def delete_source(source: str) -> None:
    initialize_collection()

    client.delete(
        collection_name=COLLECTION_NAME,
        points_selector=FilterSelector(
            filter=Filter(
                must=[
                    FieldCondition(
                        key="source",
                        match=MatchValue(value=source),
                    )
                ]
            )
        ),
        wait=True,
    )
              

def search(
    query_embedding: list[float],
    top_k: int,
    filters: RetrievalFilter | None = None,
) -> list[VectorSearchResult]:
    """search for top_k indexed chunks which matches the query embedding."""

    query_filter = None

    if filters is not None and filters.sources:
        query_filter = Filter(
            must=[
                FieldCondition(
                    key="source",
                    match=MatchAny(
                        any=filters.sources,
                    ),
                )
            ]
        )

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        query_filter=query_filter,
        limit=top_k,
        with_payload=True,
        with_vectors=False,
    )

    results: list[VectorSearchResult] = []

    for point in response.points:
        payload = point.payload

        results.append(
            VectorSearchResult(
                source=payload["source"],
                chunk_id=payload["chunk_id"],
                text=payload["text"],
                score=point.score,
            )
        )

    return results

def close_vector_store() -> None:
    client.close()