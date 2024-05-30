import os
from pinecone import Pinecone as myPinecone
from langchain_community.vectorstores import Pinecone
# from chat_services.models import ChatArgs
from embeddings.openai import embeddings

# Initialize Pinecone
pc = myPinecone(api_key=os.environ.get("PINECONE_API_KEY"))

vector_store = Pinecone.from_existing_index(
    os.environ.get("PINECONE_INDEX_NAME"), embeddings
)

def build_retriever(chat_args):
    search_kwargs = {
        "filter": { "label": chat_args.tourID },
        "k": 1
        }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )