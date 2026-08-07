import json
from pathlib import Path
from typing import Any

from chunker import chunk
from embedding_service import generate_embedding


EMBEDDINGS_FILE = Path("embeddings.json")
KNOWLEDGE_DIRECTORY = Path("knowledge")

DOCUMENTS = [
    "mongodb.md",
    "docker.md",
    "kubernetes.md",
]


def build_embedding_index() -> None:
    """Generate embeddings for new or modified document chunks."""

    existing_index = load_raw_embedding_index()
    updated_index: dict[str, dict[str, Any]] = {}

    for document_name in DOCUMENTS:
        file_path = KNOWLEDGE_DIRECTORY / document_name
        modified_at = file_path.stat().st_mtime
        content = extract_file(file_path)
        chunks = chunk(content)

        for chunk_index, chunk_text in enumerate(chunks):
            chunk_key = f"{document_name}#chunk_{chunk_index}"
            existing_entry = existing_index.get(chunk_key)

            if (
                existing_entry is not None
                and existing_entry.get("modified_at") == modified_at
                and existing_entry.get("text") == chunk_text
            ):
                updated_index[chunk_key] = existing_entry
                continue

            updated_index[chunk_key] = {
                "source": document_name,
                "chunk_index": chunk_index,
                "modified_at": modified_at,
                "text": chunk_text,
                "embedding": generate_embedding(chunk_text),
            }

    store_embedding_index(updated_index)


def load_embedding_index() -> dict[str, tuple[list[float],str] ]:
    """Load chunk identifiers and embedding vectors for retrieval."""

    raw_index = load_raw_embedding_index()

    return {
        chunk_key: (entry["embedding"], entry["text"])
        for chunk_key, entry in raw_index.items()
    }


def load_raw_embedding_index() -> dict[str, dict[str, Any]]:
    """Load persisted chunk embeddings and metadata."""

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