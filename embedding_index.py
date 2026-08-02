from embedding_service import generate_embedding
from pathlib import Path


KNOWLEDGE_DIRECTORY = Path("knowledge")
DOCUMENTS = ["mongodb.md", "docker.md", "kubernetes.md"]

def build_embedding_index() -> dict[str, list[float]]:
    indices={}
    for document in DOCUMENTS:
        file = extract_file(KNOWLEDGE_DIRECTORY / document)
        indices[document] = generate_embedding(file)
    return indices

def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()