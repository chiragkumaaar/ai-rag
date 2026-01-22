# 📖 Agentic AI RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly based on the Agentic AI eBook.  
The system retrieves relevant document chunks, generates grounded answers, and reports a confidence score.

# 🔗 Knowledge Base

Agentic AI – An Executive’s Guide to In-depth Understanding of Agentic AI  
Source PDF: https://konverge.ai/pdf/Ebook-Agentic-AI.pdf

# 🧠 Architecture Overview
PDF  
 ↓  
Text Chunking  
 ↓  
Embeddings (Sentence Transformers)  
 ↓  
ChromaDB (Vector Store)  
 ↓  
LangGraph  
   ├── Retrieve Node  
   └── Generate Node  
 ↓  
Streamlit Chat UI  

# ⚙️ Setup Instructions
## 1️⃣ Clone the Repository
git clone (https://github.com/chiragkumaaar/ai-rag.git) 
cd agentic-ai-rag
## 2️⃣ Create Virtual Environment
python -m venv venv       
venv\Scripts\activate        

## 3️⃣ Install Dependencies
pip install -r requirements.txt

## 4️⃣ Add Environment Variables
Create a .env file in the project root:  

OPENAI_API_KEY=your_openai_api_key
