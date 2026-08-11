from retriever import retrieve


def test_retrieve_mongodb() -> None:
    documents = retrieve("MongoDB connection refused")

    assert len(documents) == 1
    assert "MongoDB Troubleshooting Guide" in documents[0]


def test_retrieve_kubernetes() -> None:
    documents = retrieve("Pod entered CrashLoopBackOff")

    assert len(documents) == 1
    assert "Kubernetes Troubleshooting Guide" in documents[0]


def test_retrieve_multiple_documents() -> None:
    documents = retrieve(
        "Kubernetes pod running a Docker container cannot connect to MongoDB"
    )

    assert len(documents) == 3


def test_retrieve_no_match() -> None:
    documents = retrieve("CPU usage is unusually high")

    assert documents == []

def test_retriever_filtering() -> None:
    filters = RetrievalFilter(
        sources=["mongodb.md"]
    )

    chunks = retrieve(
        query="MongoDB connection refused",
        filters=filters,
    )

    for chunk in chunks:
        assert chunk.source == "mongodb.md"

def test_retriever_without_filter() -> None:
    chunks = retrieve("MongoDB connection refused")

    assert len(chunks) > 0