# vector_store.py

import json
from pathlib import Path

from models import IndexedChunk


EMBEDDINGS_FILE = Path("embeddings.json")


def load_chunks() -> dict[str, IndexedChunk]:
    if not EMBEDDINGS_FILE.exists():
        return {}

    with EMBEDDINGS_FILE.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    return {
        chunk_id: IndexedChunk.model_validate(entry)
        for chunk_id, entry in raw_data.items()
    }


def save_chunks(
    chunks: dict[str, IndexedChunk],
) -> None:
    serialized = {
        chunk_id: chunk.model_dump()
        for chunk_id, chunk in chunks.items()
    }

    with EMBEDDINGS_FILE.open("w", encoding="utf-8") as file:
        json.dump(serialized, file, indent=2)