from models import RetrievedChunk

def rerank(
    chunks: list[RetrievedChunk],
) -> list[RetrievedChunk]:
    return chunks