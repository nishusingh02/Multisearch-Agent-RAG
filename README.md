# LangChain Research Assistant with Wikipedia, ArXiv, and FAISS Search

## About the Project

This project is an intelligent research assistant built with [LangChain](https://www.langchain.com/) that leverages multiple data sources and tools to answer queries effectively. It integrates:

- **Wikipedia API** for fetching summarized information.
- **ArXiv API** for accessing scientific research papers.
- **LangSmith documentation** loaded and indexed with **FAISS** for similarity-based retrieval.
- OpenAI's GPT model (`gpt-3.5-turbo-0125`) to generate responses and orchestrate tool usage.

By combining these components, the assistant can provide precise, context-aware answers by dynamically choosing the best source.

---

## Features

- Query Wikipedia for quick factual information.
- Search latest research articles on ArXiv.
- Perform semantic search over LangSmith documentation.
- Use OpenAI GPT for natural language understanding and response generation.

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/nishusingh02/Multisearch-Agent-RAG>
cd <agent>
