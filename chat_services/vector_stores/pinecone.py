import os
from pinecone import Pinecone as myPinecone
from langchain_community.vectorstores import Pinecone
# from chat_services.models import ChatArgs
from chat_services.embeddings import openai

# Initialize Pinecone
pc = myPinecone(api_key=os.environ.get("PINECONE_API_KEY"))

vector_store = Pinecone.from_existing_index(
    os.environ.get("PINECONE_INDEX_NAME"), openai.embeddings
)

def build_retriever(chat_args):
    search_kwargs = {
        "filter": { "label": chat_args.tourID },
        }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )