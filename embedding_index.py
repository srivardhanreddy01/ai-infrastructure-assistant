from pathlib import Path

from chunker import chunk
from embedding_service import generate_embedding
from vector_store import delete_source, save_chunks, close_vector_store
from models import IndexedChunk

KNOWLEDGE_DIRECTORY = Path("knowledge")

DOCUMENTS = [
    "mongodb.md",
    "docker.md",
    "kubernetes.md",
]


def build_embedding_index() -> None:
    """Generate embeddings for new or modified document chunks."""
    
    for document_name in DOCUMENTS:
        file_path = KNOWLEDGE_DIRECTORY / document_name
        modified_at = file_path.stat().st_mtime

        content = extract_file(file_path)
        chunks = chunk(content)

        delete_source(document_name)
        indexed_chunks: dict[str, IndexedChunk] = {}

        for chunk_index, chunk_text in enumerate(chunks):
            chunk_id = f"{document_name}#chunk_{chunk_index}"

            indexed_chunks[chunk_id] = IndexedChunk(
                source=document_name,
                chunk_id=chunk_id,
                modified_at=modified_at,
                text=chunk_text,
                embedding=generate_embedding(chunk_text),
            )

        save_chunks(indexed_chunks)

def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    build_embedding_index()