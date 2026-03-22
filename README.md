# 📈 News Research Tool

An AI-powered news research web application that allows investors and traders to analyze stock-related news articles and websites in real-time. Users can submit up to **10 URLs** from financial news sources, and the app uses a **RAG (Retrieval-Augmented Generation)** pipeline to answer questions based on the content of those pages.



## 🔍 Overview

This tool helps investors and traders extract insights from financial news without reading through dozens of articles manually. Simply paste URLs, ask questions, and get AI-generated answers with sources — all in real-time.

---

## ✨ Features

- 🌐 Accepts up to **10 user-provided URLs** (news articles, Wikipedia, financial sites)
- 🤖 Uses **OpenAI GPT** to answer questions based on the content of those URLs
- 🔎 **RAG pipeline** — retrieves relevant content before generating answers
- 🗂️ Stores document embeddings using **FAISS** vector store
- 💬 Chat history — keeps track of all your questions and answers in one session
- 📌 Shows **sources** used to generate each answer
- 💾 Saves the FAISS index locally using `pickle` for reuse
- 🖥️ Clean interactive interface built with **Streamlit**

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web application UI |
| OpenAI GPT | Language model for answering questions |
| LangChain | RAG pipeline and chain management |
| FAISS | Vector store for document embeddings |
| OpenAI Embeddings | Converting text into vectors |
| UnstructuredURLLoader | Loading content from URLs |
| dotenv | Managing environment variables |
| pickle | Saving and loading FAISS index |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/123modelname/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never share your `.env` file. It is already listed in `.gitignore`.
> You can get your OpenAI API key from [platform.openai.com](https://platform.openai.com)

### 4. Run the App

```bash
streamlit run testapp.py
```

---

## 📖 How to Use

1. Launch the app with `streamlit run testapp.py`
2. In the **sidebar**, paste up to **10 URLs** from stock-related websites
3. Click **"Process URLs"** — the app will load, split, and embed the content
4. Type your question in the **Question box**
5. The app will return an **AI-generated answer** along with the **sources** it used
6. Your full **chat history** is displayed below for reference

---

## 📁 Project Structure

```
├── testapp.py                  # Main Streamlit application
├── faiss_store_openai.pkl      # Saved FAISS vector index (auto-generated)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not uploaded to GitHub)
├── .env.example                # Example env file (safe to share)
└── README.md                   # Project documentation
```

---

## 📦 Requirements

Create a `requirements.txt` with the following:

```
streamlit
langchain
langchain-openai
langchain-community
langchain-text-splitters
faiss-cpu
openai
unstructured
python-dotenv
```

---

## ⚠️ Disclaimer

This tool is for **educational and informational purposes only**. It does not constitute financial advice. Always consult a qualified financial advisor before making investment decisions.

---

## 👤 Author

**123modelname**  
GitHub: [github.com/123modelname](https://github.com/123modelname)
