import math

from embedding_index import load_raw_embedding_index
from embedding_service import generate_embedding
from models import IndexedChunk, RetrievedChunk


TOP_K = 3
MINIMUM_SIMILARITY = 0.45


def retrieve(query: str) -> list[RetrievedChunk]:
    """Return the top relevant knowledge chunks for the query."""

    scores = calculate_similarity_scores(query)

    if not scores:
        return []

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1][0],
        reverse=True,
    )

    top_chunks: list[RetrievedChunk] = []

    for chunk_id, (similarity_score, entry) in sorted_scores:
        if similarity_score < MINIMUM_SIMILARITY:
            continue

        top_chunks.append(
            RetrievedChunk(
                source=entry.source,
                chunk_id=chunk_id,
                text=entry.text,
                similarity_score=similarity_score,
            )
        )

        if len(top_chunks) == TOP_K:
            break

    return top_chunks


def calculate_similarity_scores(
    query: str,
) -> dict[str, tuple[float, IndexedChunk]]:
    """Calculate query similarity against indexed chunks."""

    index = load_raw_embedding_index()
    query_embedding = generate_embedding(query)

    scores: dict[str, tuple[float, IndexedChunk]] = {}

    for chunk_id, entry in index.items():
        score = cosine_similarity(
            query_embedding,
            entry.embedding,
        )

        scores[chunk_id] = (score, entry)

    return scores


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