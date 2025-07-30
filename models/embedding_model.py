from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

def setup_qdrant(collection_name: str):
    client = QdrantClient(url="http://localhost:6333")
    
    try:
        collection_info = client.get_collection(collection_name=collection_name)
    except (ValueError, Exception):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=1024, distance=Distance.COSINE),
        )
    
    return client