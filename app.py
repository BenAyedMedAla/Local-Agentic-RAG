from fastapi import FastAPI
from langchain.agents import Agent
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from utils.text_splitter import split_documents
from models.embedding_model import setup_qdrant

app = FastAPI()

# Initialize Qdrant and embeddings
client = setup_qdrant(collection_name="agent-rag")
embeddings = FastEmbedEmbeddings(model_name="thenlper/gte-large")

@app.post("/salem/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/hi/")
async def load():
    # Load and process data
    # with open('data/web_data.json', 'r') as f:
    #     data = f.read()
    
    # chunks = split_documents(data)
    print("hi")
    # # Add to Qdrant
    # vector_store = QdrantVectorStore(client=client, collection_name="agent-rag", embedding=embeddings)
    # vector_store.add_documents(documents=chunks)
    
    return {"status": "Data loaded successfully"}

@app.post("/query/")
async def query_user(input_query: str):
    # Perform query on knowledge base
    vector_store = QdrantVectorStore(client=client, collection_name="agent-rag", embedding=embeddings)
    retriever = vector_store.as_retriever()
    
    docs_content = retriever.invoke(input_query)
    context = ""
    for data in docs_content:
        context += data.page_content
    
    agent = Agent(model="Ollama")  # Example agent setup, replace with actual model
    response = agent.run(context + input_query)
    
    return {"response": response}