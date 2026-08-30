# vector_store.py

import json
import math
from pathlib import Path

from models import IndexedChunk, RetrievalFilter, VectorSearchResult


EMBEDDINGS_FILE = Path("embeddings.json")


def load_chunks() -> dict[str, IndexedChunk]:
    if not EMBEDDINGS_FILE.exists():
        return {}

    with EMBEDDINGS_FILE.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    return {
        chunk_id: IndexedChunk.model_validate(entry)
        for chunk_id, entry in raw_data.items()
    }


def save_chunks(
    chunks: dict[str, IndexedChunk],
) -> None:
    serialized = {
        chunk_id: chunk.model_dump()
        for chunk_id, chunk in chunks.items()
    }

    with EMBEDDINGS_FILE.open("w", encoding="utf-8") as file:
        json.dump(serialized, file, indent=2)

def search(
    query_embedding: list[float],
    top_k: int,
    filters: RetrievalFilter | None = None,
) -> list[VectorSearchResult]:
    """search for top_k indexed chunks which matches the query embedding."""

    index = load_chunks()
    result = []
    for chunk_id, entry in index.items():
        if (
        filters is not None
        and filters.sources is not None
        and entry.source not in filters.sources
        ):
            continue

        score = cosine_similarity(
            query_embedding,
            entry.embedding,
        )

        result.append(VectorSearchResult(chunk = entry, score = score))
    
    sorted_vectorsearch = sorted(
        result,
        key=lambda result: result.score,
        reverse=True,
    )

    return results[:top_k]

def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """Calculate cosine similarity between two vectors."""

    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions.")

    dot_product = sum(
        x * y for x, y in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(x**2 for x in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(y**2 for y in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot compare zero-length vectors.")

    return dot_product / (magnitude_a * magnitude_b)