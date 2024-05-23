import os
from pinecone import Pinecone as myPinecone
from pinecone import ServerlessSpec
from langchain_community.vectorstores import Pinecone
from models import ChatArgs
from embeddings.openai import embeddings

# Initialize Pinecone
pc = myPinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# Now do stuff
if 'testindex' not in pc.list_indexes().names():
    pc.create_index(
        name='testindex', 
        dimension=1536, 
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='gcp',
            region='us-central1'
        )
    )

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)

def build_retriever(sourceID: str):
    search_kwargs = {"filter": { "source": sourceID }}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )