
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DB_PATH = "chroma_db"


# STEP 1: Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("PDF loaded successfully!")
print("Total pages:", len(documents))


# STEP 2: Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print("Text splitting completed!")
print("Total chunks:", len(chunks))


# STEP 3: Generate embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embeddings generated!")


# STEP 4: Store in ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("Documents stored in ChromaDB successfully!")


# STEP 5: Test document retrieval
question = "What is Machine Learning?"

results = vectorstore.similarity_search(
    question,
    k=3
)

print("\nRetrieved Results:")

for result in results:
    print("\nContent:", result.page_content)
    print("Page:", result.metadata.get("page"))

print("\nRAG pipeline completed!")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating database...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("Documents stored successfully!")

question = "What is Machine Learning?"

results = vectorstore.similarity_search(question, k=3)

print("\nRetrieved Results:")

for result in results:
    print(result.page_content)
