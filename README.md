# Project Argus

> A modular AI runtime for orchestrating intelligent agents, tools, memory, and multiple language model providers.

**Current Version:** v0.3.0

---

# Vision

Project Argus is an open-source AI runtime focused on building reliable, maintainable, and extensible AI systems.

Rather than being a single chatbot, Argus is designed to become an operating system for AI—capable of coordinating specialized agents, interacting with external services, executing complex workflows, and seamlessly switching between local and cloud language models.

The project is being built from the ground up using production-quality software engineering practices with an emphasis on modular architecture, readability, testing, maintainability, and long-term extensibility.

---

# Current Status

**Stage:** Early Development (v0.3.0)

## Completed

- ✅ Project architecture established
- ✅ Environment configuration
- ✅ Modular Python package structure
- ✅ Git & GitHub workflow
- ✅ AI provider abstraction layer
- ✅ OpenAI provider
- ✅ Ollama provider
- ✅ ProviderFactory
- ✅ Local LLM support
- ✅ Centralized provider exception handling

## Currently Building

- 🚧 Argus Engine

## Upcoming Milestones

- Memory system
- Tool execution framework
- Agent framework
- Conversation management
- Workflow orchestration

---

# Design Principles

Project Argus is intentionally built around clean architecture principles.

Core design goals include:

- Provider-independent AI integration
- Loose coupling
- Dependency inversion
- Modular components
- High testability
- Clear separation of responsibilities
- Incremental development
- Long-term maintainability

---

# Goals

Project Argus aims to provide:

- Modular AI agent architecture
- Provider-independent LLM support
- Local and cloud model compatibility
- Memory and context management
- Extensible tool system
- Workflow orchestration
- Autonomous task execution
- Production-ready Python architecture
- Comprehensive documentation

---

# Current Architecture

```
                 Project Argus

                      │
                      ▼
               ProviderFactory
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   OpenAIProvider          OllamaProvider
          │                       │
          ▼                       ▼
     OpenAI API            Local Ollama
```

---

# Planned Architecture (Brick #4)

```
                 Project Argus

                      │
                      ▼
                 Argus Engine
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
   Memory          Providers        Tools
                      │
             ┌────────┴────────┐
             ▼                 ▼
        OpenAI           Ollama
```

---

# Project Structure

```
Project-Argus/
│
├── app/
│   ├── agents/
│   ├── core/
│   │   └── config.py
│   ├── models/
│   ├── providers/
│   │   ├── base.py
│   │   ├── exceptions.py
│   │   ├── factory.py
│   │   ├── ollama_provider.py
│   │   └── openai_provider.py
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── docs/
│   └── development-journal.md
│
├── tests/
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

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
- Docker
- PostgreSQL
- Redis
- LangGraph (evaluation)
- OpenTelemetry
- Pytest

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

## Configure the provider

### OpenAI

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=your_model
AI_PROVIDER=openai
```

### Ollama (Local)

```env
AI_PROVIDER=ollama
OLLAMA_MODEL=llama3.2:3b
```

Run Project Argus:

```bash
python -m app.main
```

---

# Roadmap

## ✅ Completed

- [x] Project initialization
- [x] Configuration management
- [x] Package architecture
- [x] Provider abstraction
- [x] OpenAI provider
- [x] Ollama provider
- [x] ProviderFactory
- [x] Local AI support

## 🚧 In Progress

- [ ] Argus Engine

## 📋 Planned

- [ ] Memory system
- [ ] Tool execution framework
- [ ] Agent framework
- [ ] Conversation management
- [ ] Workflow orchestration
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] REST API
- [ ] Web interface
- [ ] Autonomous multi-agent execution

---

# Development Philosophy

Project Argus is being built as if it were a production software platform rather than a prototype.

Every major feature follows the same development process:

1. Design
2. Implementation
3. Testing
4. Documentation
5. Git versioning
6. Development journal updates

The goal is not simply to build an AI application, but to engineer a maintainable platform that can continue to grow over time.

---

# License

MIT License

---

# Author

Built by **Matthew Hugues** as an ongoing exploration of modern AI software engineering, autonomous systems, clean architecture, and production-ready Python development.
