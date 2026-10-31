
from pathlib import Path

from langchain.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Load the existing ChromaDB database
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embeddings
)


# TOOL 1: Course PDF Retrieval
@tool
def course_retrieval_tool(question: str) -> str:
    """Find answers to academic questions using the uploaded course PDF."""

    results = vectorstore.similarity_search(question, k=3)

    if not results:
        return "No relevant information found in the course PDF."

    answer = ""

    for doc in results:
        answer += (
            f"\nPage: {doc.metadata.get('page', 'Unknown')}\n"
            f"Content: {doc.page_content}\n"
        )

    return answer


# TOOL 2: Career Opportunity Search
@tool
def career_search_tool(topic: str) -> str:
    """Find sample learning and career opportunities related to a skill or topic."""

    opportunities = [
        {
            "title": "Python Developer Internship",
            "skills": "python programming coding",
            "type": "Sample internship"
        },
        {
            "title": "Machine Learning Project",
            "skills": "machine learning python artificial intelligence",
            "type": "Sample learning opportunity"
        },
        {
            "title": "Data Analyst Learning Path",
            "skills": "data analysis python sql statistics",
            "type": "Sample learning opportunity"
        },
        {
            "title": "Web Development Internship",
            "skills": "html css javascript web development",
            "type": "Sample internship"
        }
    ]

    words = topic.lower().split()
    matches = []

    for item in opportunities:
        if any(word in item["skills"] for word in words):
            matches.append(item)

    if not matches:
        return "No matching sample opportunities found."

    return "\n".join(
        f"Title: {item['title']}\n"
        f"Type: {item['type']}\n"
        f"Skills: {item['skills']}"
        for item in matches
    )
