<div align="center">

# 📚 Advanced RAG System

### *Intelligent Document Q&A powered by AI*

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Demo Video](https://drive.google.com/file/d/1u1by62j8OaY3srCORFj7m0XsGutu3-0Y/view?usp=sharing) • [Report Bug](https://github.com/choudharikiranv15/Advanced-RAG-System/issues) • [Request Feature](https://github.com/choudharikiranv15/Advanced-RAG-System/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
- [Docker Setup](#-docker-setup)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

**Advanced RAG System** is a production-ready Retrieval-Augmented Generation application that enables intelligent question-answering over your PDF documents. Upload your documents and get accurate, context-aware answers powered by state-of-the-art AI.

### What is RAG?

Retrieval-Augmented Generation (RAG) combines the power of information retrieval with large language models to provide accurate, source-backed answers to your questions. This system extracts content from your documents, indexes it intelligently, and uses AI to generate comprehensive responses.

### Why This RAG System?

- 🚀 **Production-Ready** - Docker support, error handling, and logging
- 🧠 **Smart Retrieval** - Query classification and context-aware search
- 📊 **Multi-Modal** - Handles text, tables, and images (with OCR)
- 💬 **ChatGPT-Style UI** - Modern, responsive interface with markdown rendering
- 🔒 **Simple & Reliable** - No complex vector database dependencies
- 🎨 **Clean Architecture** - Modular design for easy customization

---

## ✨ Key Features

### 📄 Multi-Modal Document Processing
- **Text Extraction** - Intelligent chunking with configurable overlap (1000 words, 200-word overlap)
- **Table Extraction** - Converts PDF tables to structured data with both human and machine-readable formats
- **Image OCR** - Extracts text from images using Tesseract with confidence scoring
- **Smart Chunking** - Preserves context across chunk boundaries

### 🧠 Intelligent Retrieval
- **Query Classification** - Automatically detects query intent (table/image/factual/conceptual/general)
- **Context-Aware Search** - Incorporates conversation history for coherent multi-turn dialogues
- **Type-Specific Boosting** - Prioritizes relevant content types based on query analysis
- **Multi-Stage Ranking** - Vector similarity + re-ranking for optimal results

### 💬 Modern User Experience
- **ChatGPT-Style Interface** - Clean, responsive UI with markdown rendering
- **Session Management** - Multi-user support with isolated conversations
- **Real-Time Responses** - Fast query processing and answer generation
- **Confidence Scoring** - Transparency about answer reliability
- **Source Citations** - Page-level references for fact-checking

### 🔧 Developer-Friendly
- **Docker Support** - One-command deployment with containerization
- **Modular Architecture** - Easy to extend and customize components
- **Comprehensive Logging** - Debug and monitor system behavior
- **Clean Configuration** - Centralized settings management

---

## 🛠️ Tech Stack

### Backend
| Component | Technology |
|-----------|------------|
| **Language** | Python 3.11 |
| **Web Framework** | [Flask 3.0](https://flask.palletsprojects.com/) |
| **LLM** | [Groq Llama-3.1-8B-Instant](https://groq.com/) |
| **Vector Store** | Custom hash-based in-memory store (384-dim) |

### PDF Processing
| Library | Purpose |
|---------|---------|
| [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) | Image extraction and rendering |
| [pdfplumber](https://github.com/jsvine/pdfplumber) | Table extraction and structured text |
| [pytesseract](https://github.com/madmaze/pytesseract) | OCR for image text extraction |
| [Pillow](https://python-pillow.org/) | Image preprocessing and manipulation |

### Data & AI
- **[pandas](https://pandas.pydata.org/)** - Table data manipulation
- **[numpy](https://numpy.org/)** - Numerical operations
- **[transformers](https://huggingface.co/docs/transformers/)** - HuggingFace ecosystem support
- **[sentence-transformers](https://www.sbert.net/)** - Available for advanced embeddings

### Frontend
- **Vanilla JavaScript** - Dynamic UI interactions
- **[marked.js](https://marked.js.org/)** - Markdown rendering
- **Custom CSS** - ChatGPT-inspired design

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Flask Web Server                        │
│              (Session Management + REST API)                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    RAG System Orchestrator                   │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────┐  ┌──────────────┐  ┌──────────────┐
│     PDF     │  │    Smart     │  │     LLM      │
│  Processor  │  │  Retriever   │  │   Handler    │
│             │  │              │  │              │
│ • Text      │  │ • Query      │  │ • Groq API   │
│ • Tables    │  │   Type       │  │ • Prompt     │
│ • Images    │  │ • Context    │  │   Engineering│
│ • OCR       │  │ • Boosting   │  │ • Markdown   │
└──────┬──────┘  └──────┬───────┘  └──────────────┘
       │                │
       │         ┌──────▼───────┐
       └────────►│    Vector    │
                 │    Store     │
                 │ (In-Memory)  │
                 └──────────────┘
```

### Data Flow

**Indexing Pipeline:**
```
PDF Upload → Content Extraction → Chunking → Embedding → Storage
```

**Query Pipeline:**
```
User Question → Query Classification → Context Enhancement →
Vector Search → Re-Ranking → LLM Generation → Formatted Response
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11** or higher
- **Tesseract OCR** (for image text extraction)
  - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
  - macOS: `brew install tesseract`
  - Linux: `sudo apt-get install tesseract-ocr`
- **Groq API Key** - Get one free at [console.groq.com](https://console.groq.com/)

### Installation

#### Option 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/choudharikiranv15/Advanced-RAG-System.git
   cd Advanced-RAG-System
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv rag_env
   rag_env\Scripts\activate

   # macOS/Linux
   python3 -m venv rag_env
   source rag_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env

   # Edit .env and add your Groq API key
   # GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   python app_flask.py
   ```

6. **Open your browser**

   Navigate to `http://localhost:8080`

#### Option 2: Docker Installation

1. **Build the Docker image**
   ```bash
   docker build -t rag-system:latest .
   ```

2. **Run with environment file** (recommended)
   ```bash
   docker run -p 8080:8080 --env-file .env rag-system:latest
   ```

   **Or pass API key directly:**
   ```bash
   docker run -p 8080:8080 -e GROQ_API_KEY=your_key_here rag-system:latest
   ```

3. **Access the application**

   Open `http://localhost:8080` in your browser

### Configuration

Create a `.env` file in the project root with the following:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional (defaults provided)
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=llama-3.1-8b-instant
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=5
```

**Getting a Groq API Key:**
1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create and copy your API key

---

## 📖 Usage Guide

### Quick Start

1. **Upload Documents**
   - Click the upload area or drag-and-drop PDF files
   - Maximum file size: 50MB per document
   - Supports multiple simultaneous uploads

2. **Ask Questions**
   - Type your question in the chat input
   - Press Enter or click Send
   - Wait for AI-generated response

3. **Explore Features**
   - **Clear Chat** - Reset conversation history
   - **View Stats** - See document processing metrics
   - **Check Sources** - Review cited page numbers

### Example Questions

Try asking questions like:

- 📊 **Tables**: *"What are the sales figures shown in the table?"*
- 🖼️ **Images**: *"Describe the diagram on page 5"*
- 📝 **Factual**: *"When was the company founded?"*
- 💡 **Conceptual**: *"Explain the main argument of this paper"*
- 🔍 **General**: *"Summarize the key points of chapter 3"*

### Understanding Responses

Each response includes:

- **📄 Answer** - Markdown-formatted response with sections and formatting
- **🎯 Confidence Score** - Reliability indicator (0-100%)
- **📚 Sources Used** - Number of document chunks referenced
- **🏷️ Query Type** - Detected intent (table/image/factual/etc.)
- **📌 Page Citations** - Referenced page numbers

---

## 📁 Project Structure

```
rag_system/
│
├── 🌐 app_flask.py              # Flask web server & API endpoints
├── 📄 templates/
│   └── index.html               # ChatGPT-style frontend UI
│
├── 🧠 src/                      # Core business logic
│   ├── rag_system.py            # Main orchestrator
│   ├── pdf_processor.py         # Multi-modal PDF extraction
│   ├── simple_vector_store.py   # In-memory vector database
│   ├── retriever.py             # Smart retrieval engine
│   └── llm_handler.py           # LLM response generation
│
├── ⚙️ config/
│   └── config.py                # Centralized configuration
│
├── 💾 data/
│   ├── pdfs/                    # Uploaded PDF storage
│   └── chroma_db/               # Legacy vector DB (unused)
│
├── 🔧 models/                   # Local embedding models
│
├── 🐳 Dockerfile                # Container deployment config
├── 📦 requirements.txt          # Python dependencies
├── 🔐 .env.example              # Environment template
└── 📖 README.md                 # This file
```

### Key Components

| File | Lines | Description |
|------|-------|-------------|
| `app_flask.py` | 118 | REST API, session management, file uploads |
| `src/rag_system.py` | 130 | Coordinates all components, main workflow |
| `src/pdf_processor.py` | 211 | Extracts text, tables, images with OCR |
| `src/simple_vector_store.py` | 104 | Hash-based vector embeddings and search |
| `src/retriever.py` | 137 | Query classification and smart ranking |
| `src/llm_handler.py` | 198 | Groq API integration, prompt engineering |
| `templates/index.html` | 422 | Modern UI with markdown rendering |

---

## 🔧 Troubleshooting

### Common Issues

<details>
<summary><b>Application won't start</b></summary>

**Symptoms:** Server fails to start or crashes immediately

**Solutions:**
- Verify Python 3.11 is installed: `python --version`
- Ensure virtual environment is activated
- Install all dependencies: `pip install -r requirements.txt`
- Check for port conflicts (8080 already in use)
</details>

<details>
<summary><b>Groq API errors</b></summary>

**Symptoms:** "API key not configured" or authentication errors

**Solutions:**
- Verify `.env` file exists in project root
- Check `GROQ_API_KEY` is set correctly (no quotes, no spaces)
- Ensure API key is valid at [console.groq.com](https://console.groq.com/)
- Restart application after changing `.env`
</details>

<details>
<summary><b>PDF upload fails</b></summary>

**Symptoms:** Upload errors or processing failures

**Solutions:**
- Check file size (max 50MB)
- Ensure file is a valid PDF (not corrupted)
- Verify `data/pdfs/` directory exists and is writable
- Check terminal for specific error messages
</details>

<details>
<summary><b>Tesseract OCR errors</b></summary>

**Symptoms:** "Tesseract not found" or OCR failures

**Solutions:**
- Install Tesseract OCR system-wide
- Windows: Add Tesseract to PATH
- Verify installation: `tesseract --version`
- Update path in code if custom installation
</details>

<details>
<summary><b>Low confidence or poor answers</b></summary>

**Symptoms:** Answers are vague or marked as low confidence

**Solutions:**
- Upload more relevant documents
- Rephrase question to be more specific
- Check if content is actually in the PDFs
- Verify document processing completed successfully
</details>

### Debug Mode

Enable detailed logging by setting in `.env`:
```env
FLASK_DEBUG=1
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to new functions/classes
- Update README if adding new features
- Test thoroughly before submitting PR

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Kiran V Choudhari**

- GitHub: [@choudharikiranv15](https://github.com/choudharikiranv15)
- Project Link: [https://github.com/choudharikiranv15/Advanced-RAG-System](https://github.com/choudharikiranv15/Advanced-RAG-System)

---

## 🙏 Acknowledgments

This project leverages amazing open-source technologies:

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Groq](https://groq.com/) - LLM inference platform
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF processing
- [pdfplumber](https://github.com/jsvine/pdfplumber) - Table extraction
- [pytesseract](https://github.com/madmaze/pytesseract) - OCR engine
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - OCR by Google
- [HuggingFace](https://huggingface.co/) - Transformers ecosystem
- [marked.js](https://marked.js.org/) - Markdown rendering

---

<div align="center">

**[⬆ Back to Top](#-advanced-rag-system)**

Made with ❤️ by [Kiran V Choudhari](https://www.linkedin.com/in/kiranchoudhari-1510m)

⭐ Star this repo if you find it helpful!

</div>
