# LangChain Research Assistant with Wikipedia, ArXiv, and FAISS Search

## 📘 About the Project

This project is an intelligent research assistant built using [LangChain](https://www.langchain.com/). It leverages multiple tools and data sources to provide accurate and context-aware answers to user queries. It integrates:

* 🌐 **Wikipedia API** — for summarized encyclopedic information
* 📚 **ArXiv API** — for scientific research papers
* 🔎 **FAISS** — for similarity search over LangSmith documentation
* 🤖 **OpenAI GPT (`gpt-3.5-turbo-0125`)** — for generating natural language responses and reasoning

By combining these components, the agent dynamically selects the most relevant tools to fulfill complex queries.

---

## 🚀 Features

* Search and summarize facts using **Wikipedia**
* Retrieve scientific papers via **ArXiv**
* Perform **semantic search** on LangSmith docs using **FAISS**
* Automatically selects tools using **LangChain OpenAI Agent**

---

## 📁 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nishusingh02/Multisearch-Agent-RAG.git
cd Multisearch-Agent-RAG
```

### 2. **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### 3. **Install Required Packages**

```bash
pip install langchain langchain_community langchain_openai langchain_text_splitters faiss-cpu python-dotenv
```

> **Note:**
>
> * `faiss-cpu` is the CPU-only version of FAISS. For GPU support, install `faiss-gpu` (requires CUDA).
> * `langchain_community` contains tools like `WikipediaAPIWrapper` and `ArxivAPIWrapper`.

### 4. **Set Up Environment Variables**

Create a `.env` file in the project root and add the following:

```env
OPENAI_API_KEY=your_openai_api_key_here
WIKIPEDIA_USER_AGENT=your_custom_user_agent
```

### 5. **Run the Application**

```bash
python agent.py
```

---

## 🔧 Usage Example

Once running, the agent will process queries like:

```text
give archives of the research paper audio super resolution using cnn
```

It will smartly use Wikipedia, ArXiv, and LangSmith FAISS search to provide a contextual and accurate response.

---

## 🎉 Credits

Developed by Nishu Singh using LangChain + OpenAI + FAISS + ArXiv + Wikipedia APIs.
