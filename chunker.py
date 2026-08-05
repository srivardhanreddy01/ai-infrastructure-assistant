def chunk(document: str) -> list[str]:
    return [
    chunk.strip()
    for chunk in document.split("## Issue")
    if chunk.strip()
    ]