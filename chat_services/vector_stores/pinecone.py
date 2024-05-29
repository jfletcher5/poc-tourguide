import os
from pinecone import Pinecone as myPinecone
from pinecone import ServerlessSpec, PodSpec
from langchain_community.vectorstores import Pinecone
#from chat_services.models import ChatArgs
from chat_services.embeddings.openai import embeddings

# Initialize Pinecone
pc = myPinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# Create if it doesn't exist
# if "try2" not in pc.list_indexes().names():
#     pc.create_index(
#         name="try2",
#         dimension=1536,
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud="aws",
#             region="us-east-1"
#         )
#     )

vector_store = Pinecone.from_existing_index(
    os.environ.get("PINECONE_INDEX_NAME"), embeddings
    # "try2", embeddings 
)

def build_retriever(sourceID: str):
    search_kwargs = {"filter": { "source": sourceID }}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )