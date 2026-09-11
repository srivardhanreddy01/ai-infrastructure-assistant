## What problem is this application solving?

Infrastructure and application logs are often large, noisy, and difficult to interpret quickly.

This project helps engineers analyze infrastructure logs using Large Language Models by identifying likely root causes, estimating severity, counting deterministic error signals, retrieving relevant troubleshooting knowledge, and suggesting recommended actions.

## Why am I building it?

The primary goal of this project is to learn AI Engineering by building a real application instead of isolated demonstrations.

Through incremental development, I want to understand how production AI systems are designed, including structured outputs, tool calling, retrieval-augmented generation, semantic search, agent workflows, evaluation, observability, and deployment.

This repository also serves as a portfolio project demonstrating the evolution of a modern AI application.

---

## Architecture Evolution

### v0.1.0 — LLM Log Analysis Foundation

```text
Log File
   ↓
Application
   ↓
Context Builder
   ↓
LLMRequest
   ↓
OpenAI Responses API
   ↓
Tool Request
   ↓
Application Executes count_errors()
   ↓
Tool Result
   ↓
OpenAI Responses API
   ↓
Validated LogAnalysis
   ↓
Console Output
```

### v0.1.0 Design Decisions

- Separate context construction from provider communication.
- Use Pydantic models as typed application contracts.
- Use deterministic application tools for exact operations.
- Use the LLM for interpretation, reasoning, and summarization.
- Keep OpenAI-specific code isolated from the main application workflow.
- Return structured application data instead of free-form text.

---

### v0.2.0 — Semantic Retrieval and RAG

```text
Knowledge Documents
   ↓
Embedding Index Builder
   ↓
OpenAI Embedding Service
   ↓
Persisted Embedding Index
   ↓
Application Reads Log File
   ↓
Semantic Retriever
   ├── Generate Query Embedding
   ├── Load Stored Document Embeddings
   ├── Calculate Cosine Similarity
   └── Select Relevant Document
   ↓
Context Builder
   ├── Stable Instructions
   ├── Retrieved Knowledge
   └── Infrastructure Logs
   ↓
LLMRequest
   ↓
OpenAI Responses API
   ↓
Optional Tool Request
   ↓
Application Executes Tool
   ↓
Validated LogAnalysis
   ↓
Console Output
```

### v0.2.0 Design Decisions

- Separate document ingestion from query-time retrieval.
- Generate document embeddings once and persist them.
- Generate only the query embedding during retrieval.
- Regenerate embeddings only for new or modified knowledge files.
- Keep the retriever independent of prompt formatting and LLM response generation.
- Use cosine similarity for semantic document ranking.
- Apply a similarity threshold to avoid injecting unrelated knowledge.
- Keep the context builder responsible for formatting retrieved knowledge for the LLM.
- Preserve the existing `retrieve(query)` interface while replacing keyword matching with semantic search.

## Current Design Pipelines

### INGESTION PIPELINE

Knowledge Documents
        ↓
      Chunker
        ↓
Embedding Service
        ↓
   IndexedChunk
        ↓
Embedding Index Builder
        ↓
    Vector Store
        ↓
        Qdrant
        ├── vectors
        └── payload metadata

### QUERY PIPELINE

User Query / Logs
        ↓
Embedding Service
        ↓
  Query Embedding
        ↓
     Retriever
        ↓
 Vector Store.search()
        │
      Qdrant
        ├── metadata filtering
        ├── vector search
        └── Top-K
        ↓
VectorSearchResult[]
        ↓
     Retriever
        │
        ├── Similarity Threshold
        └── Convert to RetrievedChunk
        ↓
 RetrievedChunk[]
        ↓
     Reranker
  (identity placeholder)
        ↓
  Context Builder
        ↓
       LLM

### Retrieval Data Models

**IndexedChunk**
Represents searchable knowledge stored by the vector store. Contains the
chunk text, source metadata, chunk identifier, and embedding.

**VectorSearchResult**
Represents the raw result returned by the vector-store search layer.
Contains an IndexedChunk and its similarity score.

**RetrievedChunk**
Represents an application-level retrieval result. Contains only the
information required by downstream retrieval and context-building stages.

### Vector Store Abstraction

The retrieval layer does not directly load or search persisted embeddings.

Instead, it interacts with the vector store through a search interface:

    search(query_embedding, top_k, filters)

### Vector Store

The vector-store layer encapsulates the underlying vector database.

The current implementation uses Qdrant for vector persistence,
similarity search, metadata filtering, and Top-K retrieval.

Application layers do not depend directly on Qdrant-specific models
or APIs. The Retriever supplies a query embedding, retrieval filters,
and the requested candidate count through the vector-store search
interface.

The vector-store layer converts Qdrant search results into
application-defined `VectorSearchResult` objects.

IndexedChunk
    → ingestion/storage representation
    → contains embedding

Qdrant Point
    → database representation
    → ID + vector + payload

VectorSearchResult
    → search boundary
    → source + chunk_id + text + score
    → no embedding
    
---

## Current Components

### Application Layer

- Reads infrastructure logs.
- Coordinates retrieval, request construction, model execution, and output.

### Context Builder

- Defines stable model instructions.
- Combines retrieved knowledge with the current log input.
- Produces an `LLMRequest`.

### Retriever

- Generates a query embedding.
- Loads persisted document embeddings.
- Calculates similarity scores.
- Selects relevant knowledge.

### Embedding Service

- Communicates with the embedding provider.
- Converts text into embedding vectors.
- Does not perform retrieval or ranking.

### Embedding Index

- Generates embeddings for knowledge documents.
- Stores embeddings with document metadata.
- Reuses unchanged embeddings.
- Regenerates embeddings for modified documents.

### LLM Provider Layer

- Communicates with the OpenAI Responses API.
- Handles tool-call requests.
- Returns a validated `LogAnalysis`.

### Domain Models

- `LLMRequest`
- `LogAnalysis`
- `Severity`

---

## Current Scope — v0.2.0

### Current Features

- OpenAI Responses API integration
- Environment-based configuration
- Typed request and response models
- Structured outputs with Pydantic
- Deterministic tool calling
- Infrastructure log analysis
- Local troubleshooting knowledge base
- Embedding generation
- Persisted embedding index
- Incremental index updates
- Cosine-similarity ranking
- Semantic retrieval
- Basic retrieval-augmented generation

### Out of Scope

- Vector database integration
- Document chunking
- Top-K retrieval
- Metadata filtering
- Hybrid retrieval
- Reranking
- MCP integration
- Agent workflows
- Persistent conversational memory
- Retrieval evaluation
- Production deployment
- Production observability