from openai_client import client

def generate_embedding(text: str) -> list[float]:
    if not text.strip():
        raise ValueError("Text must not be empty.")

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    if not response.data:
        raise RuntimeError("Embedding API returned no data.")

    return response.data[0].embedding