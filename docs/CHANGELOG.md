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