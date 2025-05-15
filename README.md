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
git clone https://github.com/nishusingh02/Multisearch-Agent-RAG.git
cd Multisearch-Agent-RAG

**2. Create and activate a virtual environment**

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

**3. Install Packages **

pip install langchain langchain_community langchain_openai langchain_text_splitters faiss-cpu python-dotenv

Note:

faiss-cpu is the CPU-only version of FAISS. If you want GPU support, install faiss-gpu instead, but it requires CUDA setup.
The langchain_community package contains community-contributed tools like WikipediaAPIWrapper and ArxivAPIWrapper.

**Set up environment variables**
Create a .env file in the project root and add your OpenAI API key and Wikipedia user agent
OPENAI_API_KEY=your_openai_api_key_here
WIKIPEDIA_USER_AGENT=your_custom_user_agent

**Run**
python main.py
