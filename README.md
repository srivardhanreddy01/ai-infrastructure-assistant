# ai-infrastructure-assistant

## Goals

- Learn AI Engineering through building
- Understand modern LLM application architecture
- Build production-quality AI systems
- Explore RAG, MCP, tool calling, and agent workflows


## Roadmap

### v0.1
- [x] Project structure
- [ ] OpenAI integration
- [ ] Prompt architecture
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

## Architecture


User
   │
   ▼
Python Application
   │
   ▼
Prompt Builder
   │
   ▼
OpenAI API
   │
   ▼
Response