from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_db import get_chroma
import os

PDF_PATH = "agentic_ai_ebook.pdf"

def ingest_pdf():
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError("PDF file not found")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    vectordb = get_chroma()
    vectordb.add_documents(chunks)
