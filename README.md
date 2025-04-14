
# 🧭 ContextCraft: Modular AI Answers from Custom Sources

ContextCraft is an interactive AI-powered assistant that lets you query your own data using retrieval-augmented generation patterns. Whether you're dealing with plain text, PDFs, databases, or knowledge graphs, ContextCraft makes it easy to extract answers using relevant, grounded context.

Think of it as your own private ChatGPT that actually knows your data.

<p align="center">
  <img src="images/contextcraft-ui.png" alt="ContextCraft UI Preview"/>
</p>

---

## 🧩 Project Overview

Instead of relying on generic model hallucinations, ContextCraft narrows down answers to what actually matters: **your content**.

ContextCraft supports:
- **Vector Retrieval** for semantic document search
- **Graph Traversal** for concept mapping and contextual expansion
- **Multi-source Hybrid Queries** that combine structure and semantics

It is powered by a clean Streamlit interface and an internal pipeline that dynamically builds the context window for LLMs to generate grounded, relevant responses.

---

## ⚙️ Features

- **Plug-and-query**: Load text, notes, URLs, or files directly into the app
- **Vector Search**: Embedding-based search to return the most semantically relevant snippets
- **Graph Mode**: Visual concept navigation and path-based contextual discovery
- **Multi-modal Indexing**: Supports plain text, HTML, Markdown, PDFs, and structured concepts
- **Docker or Virtual Environment**: Choose how you run it, no lock-in
- **Interactive Exploration**: Preview matched content and graph structures before generating answers

---

## 📥 Installation Instructions

### Option 1: Docker (Recommended)

```bash
docker run -d -p 8601:8601 --gpus=all ghcr.io/your-org/contextcraft
```

### Option 2: Python Virtual Environment

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
streamlit run contextcraft.py
```

---

## 🔑 Example Queries

| Query Type                  | Example                                             |
|----------------------------|-----------------------------------------------------|
| Vector RAG                 | `What is the mission of OpenAI?`                   |
| Graph RAG                  | `gq: How does neural architecture relate to GPT-4?` |
| Concept Path               | `deep learning -> transformers -> GPT`             |
| Hybrid                     | `gq: Summarize GPT-4 evolution deep learning -> GPT`|

Use `gq:` to trigger graph-based semantic expansion before LLM generation.

---

## 🧠 How It Works

ContextCraft combines multiple retrieval engines:
1. **Embeddings Index**: Stores vectorized document fragments
2. **Concept Graph**: Links related ideas, paragraphs, or entities
3. **LLM Pipeline**: Dynamically prompts a model based on selected context

For hybrid queries, the graph expands around a concept, filters relevant nodes, and optionally narrows context using vector search.

---

## 📁 Adding Data

Add data directly from the interface or the command line.

### Upload File or URL

```bash
# File or URL
# ./uploads/notes.pdf
# https://en.wikipedia.org/wiki/Neural_network
```

### Input Inline Text

```bash
#text: ContextCraft is a modular AI tool that enables hybrid context retrieval
```

Each entry is chunked, indexed, and labeled with auto-generated topics.

---

## 🔧 Configuration

| Variable         | Description                                  | Default                         |
|------------------|----------------------------------------------|---------------------------------|
| `APP_TITLE`       | Display title of the UI                      | ContextCraft                    |
| `DEFAULT_EXAMPLES`| Semicolon-separated starter queries          | `What is a language model?`     |
| `LLM_MODEL`       | Model alias or endpoint                      | `gpt-3.5-turbo`                 |
| `EMBEDDING_MODEL` | Embedding model to use for indexing          | `sentence-transformers/all-MiniLM-L6-v2` |
| `GRAPH_ENABLED`   | Enable or disable graph context mode         | `true`                          |
| `DATA_PATH`       | Path to user data for bootstrapping index    | `./data`                        |

---

## 🧪 Test Dataset

Preloaded data includes:
- Sample Wikipedia entries on AI topics
- Custom notes with labeled nodes and edges
- Basic PDF documents for document search tests

---

## 🖥 Requirements

- Python 3.9 or newer
- Streamlit
- FAISS for vector indexing
- NetworkX or Neo4j for graph modeling
- OpenAI or HuggingFace-compatible LLM endpoint
- Docker (optional but recommended for ease)

---

## 🧾 Licensing and Acknowledgements

**License**: MIT  
Use freely, modify as needed. Contributions are welcome.

**Inspired by:**
- The RAG pattern, reimagined through a hybrid context lens
- Open-source knowledge graphs and vector search libraries
- The need for a transparent and grounded approach to AI answers

---

> Knowledge grounded in your data, not the noise.

**Craft smarter context with ContextCraft.**
