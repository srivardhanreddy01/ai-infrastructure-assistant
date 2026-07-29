from pathlib import Path


KNOWLEDGE_DIRECTORY = Path("knowledge")

DOCUMENT_KEYWORDS = {
    "mongodb.md": [
        "mongodb",
        "e11000",
        "duplicate key",
        "port 27017",
    ],
    "kubernetes.md": [
        "kubernetes",
        "crashloopbackoff",
        "imagepullbackoff",
        "errimagepull",
    ],
    "docker.md": [
        "docker",
        "oomkilled",
        "exit code 137",
        "address already in use",
    ],
}


def retrieve(log_text: str) -> list[str]:
    normalized_text = log_text.lower()
    documents: list[str] = []

    for filename, keywords in DOCUMENT_KEYWORDS.items():
        if any(keyword in normalized_text for keyword in keywords):
            documents.append(
                extract_file(KNOWLEDGE_DIRECTORY / filename)
            )
    return documents


def extract_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()