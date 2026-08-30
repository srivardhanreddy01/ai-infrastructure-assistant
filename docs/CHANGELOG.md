## Unreleased

### Added 

- Typed `LogAnalysis` response model
- OpenAI Structured Outputs integration
- Response validation with Pydantic

### Changed

- LLM layer now returns typed domain objects instead of raw text.

## v0.1.0

### Added

- Initial AI Infrastructure Assistant project structure
- OpenAI Responses API integration
- File-based infrastructure log analysis
- Typed `LLMRequest` and `LogAnalysis` models
- Structured outputs using Pydantic
- Tool calling for deterministic error counting
- Basic error handling
- Initial architecture documentation
- Unit tests for deterministic tools

## Unreleased

### Added 

- retiever.py which return relevant docs based on input data
- retiever does a keyword check and returns the docs
- Context builder now uses the retrieved docs data and appends it to user input
- Added test to check the functionality of the retriever

### Changed

- Updated context builder to also support retrieved docs
- app.py now calls retiver and passes it to context builder

## v0.2.0

### Added

- Infrastructure troubleshooting knowledge base
- Keyword-based document retrieval
- OpenAI embedding generation
- Shared OpenAI client
- Semantic document retrieval
- Cosine-similarity ranking
- Persisted embedding index
- Incremental embedding regeneration for modified documents
- Retrieved knowledge injection into the LLM context

### Changed

- Replaced the original keyword-only retrieval path with semantic retrieval.
- Separated document indexing from query-time retrieval.
- Expanded the context builder to include retrieved troubleshooting knowledge.

### Known Limitations

- Documents are embedded as whole files rather than smaller chunks.
- Retrieval currently selects a single best document.
- Embeddings are stored in a local JSON file.
- No vector database or metadata filtering is implemented.

## Unreleased

### Added

- Document chunking based on issue sections
- Chunk-level embedding generation
- Typed `IndexedChunk` model
- Typed `RetrievedChunk` model
- Top-K semantic retrieval
- Minimum similarity filtering
- Metadata filtering by document source
- Retrieval metadata including source, chunk ID, and similarity score
- Reranker abstraction
- Vector-store abstraction for persistence

### Changed

- Retrieval now operates on chunks instead of entire documents.
- Embedding index now stores chunk text and metadata alongside vectors.
- Retriever now returns typed retrieval results instead of raw strings.
- Retrieval now supports multiple relevant chunks.
- Vector persistence has been separated from index-building logic.
- Context construction now consumes retrieved chunk objects instead of plain document strings.

### Architecture

- Separated ingestion-time indexing from query-time retrieval.
- Added a storage abstraction so retrieval is no longer coupled to JSON persistence.

### Changed
- Moved vector similarity search out of the retriever into the vector-store layer.
- Added a backend-independent `search()` interface for vector retrieval.
- Added `VectorSearchResult` to separate storage search results from application-level retrieval results.
- Retriever now generates query embeddings, delegates vector search, applies retrieval policy, and converts search results into `RetrievedChunk` objects.
- JSON persistence remains the current vector-store backend.