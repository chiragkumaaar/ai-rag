import streamlit as st
from graph import rag_graph

st.set_page_config(page_title="Agentic AI RAG Chatbot", layout="centered")

st.title("RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask a question about Agentic AI...")

if query:
    st.session_state.messages.append(
        {"role": "user", "content": query}
    )
    with st.chat_message("user"):
        st.markdown(query)

    result = rag_graph.invoke({"question": query})

    answer = result["answer"]
    confidence = result["confidence"]
    context = result["context"]

    response = f"""
**Answer:**  
{answer}

**Confidence:** `{confidence}`

**Retrieved Context:**
"""

    for i, chunk in enumerate(context):
        response += f"\n\n**Chunk {i+1}:**\n{chunk}"

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)
