## What problem is this application solving?
Infrastructure and application logs are often large, noisy, and difficult to interpret quickly. This project aims to help engineers analyze logs using Large Language Models (LLMs) by identifying potential root causes, estimating severity, and suggesting recommended actions.


## Why am I building it?
The primary goal of this project is to learn AI by building a real application instead of isolated demos.

Through incremental development, I want to understand how production AI systems are designed, including prompt engineering, structured outputs, tool calling, retrieval-augmented generation (RAG), agent workflows, evaluation, and deployment.

This repository also serves as a portfolio project demonstrating modern AI application architecture.


## Architecture

                +------------------+
                |      User        |
                +------------------+
                          |
                          v
                +-------------------+
                | Python Application|
                +-------------------+
                          |
                          v
                +------------------+
                | Read Log File    |
                +------------------+
                          |
                          v
                +--------------------------+
                |     Context Builder      | ----> Context Builder
                +--------------------------+
                          |                             ├── Instructions
                          |
                          |                             ├── User Question
                          |
                          |                             ├── Logs
                          |
                          |                             ├── Retrieved Docs
                          |
                          |                             ├── Tool Results
                          |
                          |                             ├── Conversation Memory
                          |
                          |
                          v
                +------------------+
                | LLM Request      |
                +------------------+
                          |
                          v
                +------------------------+
                | LLM Provider Layer     |
                +------------------------+
                          |
                          v
                +------------------+
                |      Open API    |
                +------------------+
                          |
                          v
                +---------------------+
                | Structured Response |
                +---------------------+
                          |
                          v
                +------------------+
                | Console Output   |
                +------------------+

## Design Decisions

### Separate prompt construction from provider communication

The prompt builder defines what the model should do and combines it with dynamic log content.

The LLM layer is responsible only for communicating with the model provider. This keeps application behavior separate from OpenAI-specific implementation details.

### Use a typed request object

`LLMRequest` acts as a shared contract between the prompt-building layer and the LLM provider layer. Pydantic validates that required instructions and input are present before making an API request.


## Current Scope (Week 1)

Current Features

- LLM API integration
- Prompt abstraction
- Configuration management
- Basic log analysis

Out of Scope

- RAG
- Vector databases
- MCP
- Agent workflows
- Memory
- Evaluation
- Deployment

