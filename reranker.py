from models import RetrievedChunk

def rerank(
    query: str,
    chunks: list[RetrievedChunk],
) -> list[RetrievedChunk]:
    """
    Placeholder reranker.

    Future implementations may use:
    - Cross-encoder models
    - Cohere Rerank
    - Voyage AI Rerank
    - Diversity heuristics
    """

    return chunks