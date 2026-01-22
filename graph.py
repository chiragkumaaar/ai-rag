from typing import TypedDict, List
from langgraph.graph import StateGraph
from vector_db import get_chroma
from llm import llm, PROMPT


class RAGState(TypedDict):
    question: str
    context: List[str]
    answer: str
    confidence: float


vectordb = get_chroma()


def retrieve(state: RAGState):
    results = vectordb.similarity_search_with_score(
        state["question"],
        k=10
    )

    filtered_context = []
    scores = []

    for doc, score in results:
        text = doc.page_content.strip()
        if len(text) < 200:
            continue
        if "Executive's Guide" in text:
            continue
        filtered_context.append(text)
        scores.append(score)

    if not filtered_context:
        filtered_context = [doc.page_content for doc, _ in results[:3]]
        scores = [score for _, score in results[:3]]

    confidence = round(1 - (sum(scores) / len(scores)), 3)

    return {
        "context": filtered_context,
        "confidence": confidence
    }


def generate(state: RAGState):
    context_text = "\n\n".join(state["context"])

    response = llm.invoke(
        PROMPT.format(
            context=context_text,
            question=state["question"]
        )
    )

    return {"answer": response.content}


graph = StateGraph(RAGState)

graph.add_node("retrieve", retrieve)
graph.add_node("generate", generate)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "generate")

rag_graph = graph.compile()
