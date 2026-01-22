from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

PROMPT = PromptTemplate(
    template="""
You are an AI assistant.
Answer the question using ONLY the information contained in the context.
If the answer cannot be derived from the context, say exactly:
"Answer not found in the provided document."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)
