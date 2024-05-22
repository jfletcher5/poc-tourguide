import os
import pinecone
from pinecone import Pinecone as myPinecone
from pinecone import ServerlessSpec
from langchain_community.vectorstores import Pinecone
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