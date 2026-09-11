from embedding_service import generate_embedding
from models import RetrievedChunk, RetrievalFilter
from vector_store import search

TOP_K = 3
MINIMUM_SIMILARITY = 0.45


def retrieve(
    query: str,
    filters: RetrievalFilter | None = None,
) -> list[RetrievedChunk]:
    """Return the top relevant knowledge chunks for the query."""

    query_embedding = generate_embedding(query)

    search_results = search(
        query_embedding=query_embedding,
        top_k=TOP_K,
        filters=filters,
    )

    retrieved_chunks: list[RetrievedChunk] = []

    for result in search_results:
        if result.score < MINIMUM_SIMILARITY:
            continue

        retrieved_chunks.append(
            RetrievedChunk(
                source=result.source,
                chunk_id=result.chunk_id,
                text=result.text,
                similarity_score=result.score,
            )
        )

    return retrieved_chunks