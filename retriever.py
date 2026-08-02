import math
from pathlib import Path

from embedding_index import build_embedding_index
from embedding_service import generate_embedding


KNOWLEDGE_DIRECTORY = Path("knowledge")


def retrieve(query: str) -> list[str]:
    """Retrieve the most semantically similar knowledge document."""

    scores = calculate_similarity_scores(query)

    if not scores:
        return []

    best_document = max(scores, key=scores.get)

    return [
        extract_file(KNOWLEDGE_DIRECTORY / best_document)
    ]


def calculate_similarity_scores(query: str) -> dict[str, float]:
    """Calculate similarity between a query and indexed documents."""

    indices = build_embedding_index()
    query_embedding = generate_embedding(query)

    scores: dict[str, float] = {}

    for document, document_embedding in indices.items():
        scores[document] = cosine_similarity(
            query_embedding,
            document_embedding,
        )

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


def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()