import json
from pathlib import Path

from chunker import chunk
from embedding_service import generate_embedding
from models import IndexedChunk


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
    updated_index: dict[str, IndexedChunk] = {}

    for document_name in DOCUMENTS:
        file_path = KNOWLEDGE_DIRECTORY / document_name
        modified_at = file_path.stat().st_mtime

        content = extract_file(file_path)
        chunks = chunk(content)

        for chunk_index, chunk_text in enumerate(chunks):
            chunk_id = f"{document_name}#chunk_{chunk_index}"

            existing_entry = existing_index.get(chunk_id)

            if (
                existing_entry is not None
                and existing_entry.modified_at == modified_at
                and existing_entry.text == chunk_text
            ):
                updated_index[chunk_id] = existing_entry
                continue

            updated_index[chunk_id] = IndexedChunk(
                source=document_name,
                chunk_id=chunk_id,
                modified_at=modified_at,
                text=chunk_text,
                embedding=generate_embedding(chunk_text),
            )

    store_embedding_index(updated_index)


def load_raw_embedding_index() -> dict[str, IndexedChunk]:
    """Load persisted chunks and convert them into typed models."""

    if not EMBEDDINGS_FILE.exists():
        return {}

    with EMBEDDINGS_FILE.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    return {
        chunk_id: IndexedChunk.model_validate(entry)
        for chunk_id, entry in raw_data.items()
    }


def store_embedding_index(
    index: dict[str, IndexedChunk],
) -> None:
    serialized_index = {
        chunk_id: entry.model_dump()
        for chunk_id, entry in index.items()
    }

    with EMBEDDINGS_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            serialized_index,
            file,
            indent=2,
        )


def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    build_embedding_index()