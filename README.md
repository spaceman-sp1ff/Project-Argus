# Project Argus

> **A modular AI runtime for orchestrating intelligent agents, tools, memory, and multiple language model providers.**

![Status](https://img.shields.io/badge/status-active%20development-orange)
![Version](https://img.shields.io/badge/version-v0.5.0--dev-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Vision

Project Argus is an open-source AI runtime focused on building reliable, maintainable, and extensible AI systems.

Rather than being a single chatbot, Argus is being engineered as an operating system for AI—capable of coordinating specialized agents, managing memory, executing tools, orchestrating workflows, and seamlessly switching between local and cloud language models.

Every component is being developed using production-quality software engineering practices with an emphasis on:

- Clean Architecture
- Maintainability
- Extensibility
- Testing
- Documentation
- Long-term evolution

---

# Current Status

**Current Version:** `v0.5.0-dev`

**Development Stage:** Phase 5 — Runtime Integration

**Latest Milestone:** ✅ Brick #4 Completed — Conversation Architecture & Persistence

**Current Objective:** Build the Argus Runtime that orchestrates conversations, providers, context, and persistence.

---

# Features

## Completed

- ✅ Modular project architecture
- ✅ Environment configuration
- ✅ Provider abstraction layer
- ✅ OpenAI provider
- ✅ Ollama provider
- ✅ ProviderFactory
- ✅ Argus Engine
- ✅ Conversation domain model
- ✅ Immutable Message model
- ✅ ContextBuilder
- ✅ Runtime system prompt management
- ✅ ConversationRepository abstraction
- ✅ JSON conversation persistence
- ✅ Persistent conversation loading
- ✅ Full save/load round-trip validation

---

## Currently Building

### Phase 5 — Argus Runtime

The next milestone integrates every completed component into a unified runtime.

Responsibilities include:

- Runtime orchestration
- Conversation lifecycle management
- Automatic persistence
- Provider execution
- Session management

---

# Architecture

Current architecture:

```text
                           Project Argus

                                  │
                                  ▼

                           Argus Runtime

        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼

 Conversation        ContextBuilder      Repository
        │                                      │
        ▼                                      ▼

  AI Provider                 JsonConversationRepository
        │
        ▼

 OpenAI / Ollama
```

---

# Project Structure

```text
Project-Argus/
│
├── app/
│   ├── agents/
│   ├── core/
│   │   ├── config.py
│   │   └── constants.py
│   │
│   ├── engine/
│   │
│   ├── models/
│   │   └── conversation.py
│   │
│   ├── providers/
│   │   ├── base.py
│   │   ├── exceptions.py
│   │   ├── factory.py
│   │   ├── ollama_provider.py
│   │   └── openai_provider.py
│   │
│   ├── repositories/
│   │   ├── conversation_repository.py
│   │   └── json_conversation_repository.py
│   │
│   ├── services/
│   │   └── context_builder.py
│   │
│   ├── utils/
│   └── main.py
│
├── docs/
│   └── development-journal.md
│
├── tests/
│
├── .env.example
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Design Philosophy

Project Argus follows a simple engineering philosophy.

Every feature is built as a small architectural **brick**.

Each brick introduces one clearly defined capability while leaving the project in a fully working state before moving to the next.

Architectural abstractions are introduced only when justified by the evolving codebase—not preemptively.

Core design principles include:

- Provider-independent AI integration
- Loose coupling
- Dependency inversion
- Separation of concerns
- Incremental development
- High testability
- Long-term maintainability

---

# Technology Stack

## Current

- Python 3.12+
- OpenAI SDK
- Ollama
- python-dotenv
- Pydantic
- Rich
- Git
- GitHub

## Planned

- FastAPI
- PostgreSQL
- Redis
- Docker
- Pytest
- OpenTelemetry

---

# Roadmap

## ✅ Phase 1 — Foundation

- Project initialization
- Environment configuration
- Package architecture

---

## ✅ Phase 2 — Provider Layer

- OpenAI integration
- Ollama integration
- Provider abstraction
- ProviderFactory

---

## ✅ Phase 3 — Conversation System

- Conversation model
- Message model
- ContextBuilder

---

## ✅ Phase 4 — Persistence

- Repository abstraction
- JSON persistence
- Conversation restoration

---

## 🚧 Phase 5 — Runtime

- Runtime orchestration
- Automatic persistence
- Session lifecycle
- Runtime integration

---

## 📋 Phase 6 — Tools

- Tool registry
- Function calling
- Tool execution

---

## 📋 Phase 7 — Memory

- Long-term memory
- Retrieval
- Context pruning

---

## 📋 Phase 8 — Agents

- Planner
- Researcher
- Executor
- Multi-agent orchestration

---

## 📋 Phase 9 — Security

- Encrypted persistence
- Secrets management
- Audit logging
- Secure configuration

---

## 📋 Phase 10 — Deployment

- REST API
- CLI
- Docker
- Web UI

---

# Getting Started

Clone the repository:

```bash
git clone https://github.com/spaceman-sp1ff/Project-Argus.git
cd Project-Argus
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

### OpenAI

```env
AI_PROVIDER=openai
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=your_model
```

### Ollama

```env
AI_PROVIDER=ollama
OLLAMA_MODEL=llama3.2:3b
```

Run Argus:

```bash
python -m app.main
```

---

# Development Workflow

Every feature follows the same process:

1. Design
2. Implementation
3. Testing
4. Documentation
5. Git Commit
6. Development Journal Update

This keeps every architectural brick complete before beginning the next.

---

# License

MIT License

---

# Author

Built by **Matthew Hugues** as an ongoing exploration of:

- AI Engineering
- Autonomous Systems
- Clean Architecture
- Production-ready Python
- Software Design
- Multi-Agent Systems
