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
                +------------------+
                | Python Application|
                +------------------+
                          |
                          v
                +------------------+
                | Prompt Builder   |
                +------------------+
                          |
                          v
                +------------------+
                | OpenAI API       |
                +------------------+
                          |
                          v
                +------------------+
                | LLM Response     |
                +------------------+
                          |
                          v
                +------------------+
                | Console Output   |
                +------------------+

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