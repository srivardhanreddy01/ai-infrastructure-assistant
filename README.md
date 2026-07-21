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
- [ ] Structured outputs
- [ ] Tool calling

### v0.2
- [ ] Embeddings
- [ ] Vector search
- [ ] RAG

### v0.3
- [ ] Agent workflows
- [ ] MCP integration
- [ ] Multi-tool orchestration

### v1.0
- [ ] Production deployment
- [ ] Evaluation
- [ ] Observability


## Project Structure

```text
infra-assistant/
├── app.py
├── llm.py
├── prompts.py
├── config.py
├── logs/
└── README.md
```

## Current Features

- OpenAI Responses API integration
- Environment-based API-key configuration
- Separation of application, prompt, and provider logic
- Typed `LLMRequest` contract
- Infrastructure log input from a local file
- Basic LLM-powered log analysis

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
