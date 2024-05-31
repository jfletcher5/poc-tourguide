import os
from langchain_pinecone import PineconeVectorStore as Pinecone
from langchain_openai import OpenAIEmbeddings
from chat_services.embeddings import openai

embeddings = OpenAIEmbeddings()
index_name = os.getenv("PINECONE_INDEX_NAME")
vector_store = Pinecone(
    index_name=index_name,
    embedding=embeddings,
    # namespace=namespace,
)

# take in the vstore label and k value and return the retriever for queries
def build_retriever(chat_args):
    search_kwargs = {
        "filter": { "label": chat_args.tourID },
        'k': chat_args.k,
        }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
