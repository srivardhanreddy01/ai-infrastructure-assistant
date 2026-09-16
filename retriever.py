from embedding_service import generate_embedding
from models import RetrievedChunk, RetrievalFilter
from vector_store import search

DEFAULT_TOP_K = 3
DEFAULT_MINIMUM_SIMILARITY = 0.45


def retrieve(
    query: str,
    filters: RetrievalFilter | None = None,
    top_k: int = DEFAULT_TOP_K,
    minimum_similarity: float | None = DEFAULT_MINIMUM_SIMILARITY,
) -> list[RetrievedChunk]:
    """Return the top relevant knowledge chunks for the query."""

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0.")

    query_embedding = generate_embedding(query)

    search_results = search(
        query_embedding=query_embedding,
        top_k=top_k,
        filters=filters,
    )

    retrieved_chunks: list[RetrievedChunk] = []

    for result in search_results:
        print(result.chunk_id + " : "+ str(result.score))
        if (minimum_similarity is not None and result.score < minimum_similarity):
            continue
        print()
        retrieved_chunks.append(
            RetrievedChunk(
                source=result.source,
                chunk_id=result.chunk_id,
                text=result.text,
                similarity_score=result.score,
            )
        )

    return retrieved_chunks