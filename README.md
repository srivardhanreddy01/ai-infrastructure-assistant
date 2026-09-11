# ai-infrastructure-assistant

AI Infrastructure Assistant is a portfolio project that explores how modern AI systems are built by incrementally evolving a simple LLM application into a production-ready AI assistant.

The project focuses on AI Engineering concepts including prompt architecture, structured outputs, retrieval-augmented generation (RAG), tool calling, Model Context Protocol (MCP), agent workflows, evaluation, and deployment.

## Goals

- Learn AI Engineering through building
- Understand modern LLM application architecture
- Build production-quality AI systems
- Explore RAG, MCP, tool calling, and agent workflows


## Roadmap

### v0.1
- [x] Project structure
- [x] OpenAI integration
- [x] Prompt architecture
- [x] Typed LLM request model
- [x] File-based log input
- [x] Structured outputs
- [x] Tool calling
- [x] Basic Error handling
- [x] Tests
- [x] Documentation and v0.1 release

### v0.2 — Knowledge Augmentation

- [x] Local troubleshooting knowledge base
- [x] Keyword-based retrieval
- [x] Embedding generation
- [x] Persisted embedding index
- [x] Incremental embedding updates
- [x] Cosine-similarity ranking
- [x] Semantic search
- [x] Basic retrieval-augmented generation

### v0.3 — Production Retrieval

- [x] Document chunking
- [x] Chunk-level embeddings
- [x] Typed indexed and retrieved chunks
- [x] Top-K retrieval
- [x] Similarity threshold
- [x] Metadata filtering
- [x] Reranker abstraction
- [x] Vector-store abstraction
- [x] Qdrant vector database integration
- [x] Vector-based nearest-neighbor search
- [ ] Retrieval evaluation
- [ ] Real reranking

### v0.4 — Agents and Tool Orchestration

- [ ] Agent workflows
- [ ] MCP integration
- [ ] Multi-tool orchestration

### v1.0
- [ ] Production deployment
- [ ] Evaluation
- [ ] Observability


## Project Structure
```text
ai-infrastructure-assistant/
├── docs/
│   └── architecture.md
│   └── CHANGELOG.md
├── knowledge/
│   └── docker.md
│   └── kubernetes.md
│   └── mongodb.md
├── logs/
│   └── mongodb_connection.log
├── app.py
├── config.py
├── context_builder.py
├── llm.py
├── models.py
├── tools.py
├── test_tools.py
├── requirements.txt
├── retriever.py
├── openai_client.py
├── embedding_service.py
├── embedding_index.py
├── test_retriever.py
├── embeddings.json
├── .gitignore
└── README.md
├── chunker.py
├── reranker.py
├── vector_store.py
```

## Current Features

- Chunk level document indexing
- Semantic retrieval using embeddings
- Top-K retrieval with similarity filtering
- Meta data aware retrieval
- Typed retrieval results
- Reranker abstraction
- Vector-store abstraction
- Incremental embedding updates

## Tech Stack

- Python
- OpenAI API
- Pydantic
- python-dotenv

Future:
- LangGraph
- Qdrant
- MCP
- Docker

## Setup

```bash
git clone https://github.com/srivardhanreddy01/ai-infrastructure-assistant.git
cd ai-infrastructure-assistant

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key
```

Run:

```bash
python app.py
```