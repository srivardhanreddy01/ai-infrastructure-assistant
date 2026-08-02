import json
from pathlib import Path
from typing import Any

from embedding_service import generate_embedding


EMBEDDINGS_FILE = Path("embeddings.json")
KNOWLEDGE_DIRECTORY = Path("knowledge")
DOCUMENTS = [
    "mongodb.md",
    "docker.md",
    "kubernetes.md",
]


def build_embedding_index() -> None:
    """
    Generate embeddings only for new or modified knowledge documents.
    """

    existing_index = load_raw_embedding_index()
    updated_index: dict[str, dict[str, Any]] = {}

    for document_name in DOCUMENTS:
        file_path = KNOWLEDGE_DIRECTORY / document_name
        modified_at = file_path.stat().st_mtime

        existing_entry = existing_index.get(document_name)

        if (
            existing_entry is not None
            and existing_entry.get("modified_at") == modified_at
        ):
            updated_index[document_name] = existing_entry
            continue

        content = extract_file(file_path)

        updated_index[document_name] = {
            "modified_at": modified_at,
            "embedding": generate_embedding(content),
        }

    store_embedding_index(updated_index)


def load_embedding_index() -> dict[str, list[float]]:
    """
    Load only document names and embedding vectors for retrieval.
    """

    raw_index = load_raw_embedding_index()

    return {
        document_name: entry["embedding"]
        for document_name, entry in raw_index.items()
    }


def load_raw_embedding_index() -> dict[str, dict[str, Any]]:
    """
    Load persisted embeddings and metadata.
    """

    if not EMBEDDINGS_FILE.exists():
        return {}

    with EMBEDDINGS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def store_embedding_index(
    index: dict[str, dict[str, Any]],
) -> None:
    with EMBEDDINGS_FILE.open("w", encoding="utf-8") as file:
        json.dump(index, file)


def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    build_embedding_index()