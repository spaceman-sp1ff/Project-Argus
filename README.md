# Project Argus

> **A modular AI runtime for orchestrating intelligent agents, tools, memory, and multiple language model providers.**

![Status](https://img.shields.io/badge/status-active%20development-orange)
![Version](https://img.shields.io/badge/version-v0.7.0--dev-blue)
![License](https://img.shields.io/badge/license-No license yet-red)

---

# Vision

Project Argus is an open-source AI runtime focused on building reliable, maintainable, and extensible AI systems.

Rather than being a single chatbot, Argus is being engineered as an operating system for AI—capable of coordinating specialized agents, managing memory, executing tools, orchestrating workflows, and seamlessly switching between local and cloud language models.

Every component is developed using production-quality software engineering practices with an emphasis on:

- Clean Architecture
- Maintainability
- Extensibility
- Testing
- Documentation
- Long-term evolution

---

# Current Status

**Current Version:** `v0.6.0-dev`

**Development Stage:** **Phase 7 — Long-Term Memory**

**Latest Milestone:** ✅ **Phase 6 Completed — Application Composition**

**Current Objective:**

Design and implement Argus' long-term memory subsystem while preserving the project's layered architecture and preparing the runtime for future tools, planners, and intelligent agents.

---

# Features

## Completed

### Foundation

- ✅ Modular project architecture
- ✅ Environment configuration

### Provider Layer

- ✅ Provider abstraction layer
- ✅ OpenAI provider
- ✅ Ollama provider
- ✅ ProviderFactory

### Runtime

- ✅ Argus Engine
- ✅ Argus Runtime
- ✅ Runtime orchestration
- ✅ Conversation lifecycle management
- ✅ Context construction
- ✅ Automatic persistence

### Conversation

- ✅ Conversation domain model
- ✅ Immutable Message model
- ✅ ContextBuilder

### Persistence

- ✅ ConversationRepository abstraction
- ✅ JSON conversation persistence
- ✅ Persistent conversation loading
- ✅ Full save/load validation

### Application Composition

- ✅ ArgusContainer
- ✅ Composition Root
- ✅ Runtime lifecycle management
- ✅ Lazy runtime initialization
- ✅ Dependency ownership

---

## Currently Building

### Phase 7 — Long-Term Memory

The next milestone introduces persistent memory that enables Argus to retain important information across conversations.

Initial responsibilities include:

- Memory domain model
- Memory repository
- Memory service
- Retrieval
- Runtime integration
- Context injection

---

# Architecture

Current architecture:

```text
                    Application Interface
                             │
                             ▼
                      ArgusContainer
                             │
                             ▼
                       ArgusRuntime
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼

 Conversation        ContextBuilder       Repository
        │                                       │
        ▼                                       ▼

   Argus Engine             JsonConversationRepository
        │
        ▼

 AI Provider (OpenAI / Ollama)
```

Each layer has a single responsibility.

The application entry point no longer constructs dependencies directly. Instead, it requests a fully configured runtime from the application's composition root.

---

# Project Structure

```text
Project-Argus/
│
├── app/
│   ├── agents/
│   │
│   ├── bootstrap/
│   │   ├── __init__.py
│   │   └── container.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── constants.py
│   │
│   ├── engine/
│   │
│   ├── runtime/
│   │
│   ├── models/
│   │
│   ├── providers/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
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

Project Argus follows an incremental engineering philosophy.

Rather than implementing large features all at once, every capability is introduced as a small architectural **brick**.

Each brick introduces a single responsibility while leaving the project in a fully working state before development continues.

Architectural abstractions are introduced only when justified by the evolving codebase—not preemptively.

Core design principles include:

- Separation of Concerns
- Single Responsibility Principle
- Dependency Inversion
- Loose Coupling
- Incremental Development
- High Testability
- Long-Term Maintainability

---

# Architectural Evolution

Project Argus is intentionally developed through incremental architectural milestones called **bricks**.

Every brick follows the same engineering workflow:

1. Design
2. Implementation
3. Testing
4. Documentation
5. Git Commit
6. Development Journal Update

Only after a brick is complete does development continue.

This methodology allows the architecture to evolve naturally while keeping the codebase stable, maintainable, and continuously functional.

The goal is not simply to build an AI assistant, but to engineer an extensible AI runtime capable of supporting future intelligent systems.

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

## ✅ Phase 5 — Runtime

- Runtime orchestration
- Automatic persistence
- Session lifecycle
- Engine execution isolation

---

## ✅ Phase 6 — Application Composition

- Application composition root
- ArgusContainer
- Dependency ownership
- Runtime lifecycle management
- Lazy initialization

---

## 🚧 Phase 7 — Long-Term Memory

- Memory domain
- Memory repository
- Memory service
- Retrieval
- Context injection

---

## 📋 Phase 8 — Tools

- Tool registry
- Tool execution
- Function calling
- Runtime integration

---

## 📋 Phase 9 — Planning

- Planner
- Decision making
- Tool selection
- Memory selection
- Task decomposition

---

## 📋 Phase 10 — Agents

- Specialized agents
- Multi-agent orchestration
- Agent coordination
- Workflow execution

---

## 📋 Phase 11 — Security

- Encrypted persistence
- Secrets management
- Audit logging
- Secure configuration

---

## 📋 Phase 12 — Interfaces

- REST API
- CLI
- Desktop Application
- Web UI

---

# Future Capability Modules

Project Argus is being designed around independently developed capability modules that plug into a common runtime.

Examples include:

- Cybersecurity Analysis
- SIEM Investigation
- Endpoint Monitoring
- Job Search Automation
- Home Lab Automation
- Raspberry Pi Orchestration
- AI Workflow Automation

Each module will integrate through the runtime without requiring changes to the application's core architecture.

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

Every architectural brick follows the same process:

1. Design
2. Implementation
3. Testing
4. Documentation
5. Git Commit
6. Development Journal Update

This ensures every milestone is complete before the next capability is introduced.

---

# License

MIT License

---

# Author

Built by **Matthew Hugues** as an ongoing exploration of:

- AI Engineering
- Autonomous Systems
- Clean Architecture
- Production-Ready Python
- Software Design
- Multi-Agent Systems
- Intelligent Runtime Architecture