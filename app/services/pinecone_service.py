from fastapi import Depends
from uuid import uuid4
import os
from chat_services.vector_stores.pinecone import vector_store
from chat_services.embeddings import openai

# def method to clear all vectors in the pinecone index filtered by metadata. make the default input PINECONE_INDEX_NAME but allow it to be changed
def delete_vectors_by_metadata(metadata_filter: str):
    query = ""
    
    results = vector_store.search(
        query,
        search_type="similarity",
        filter={
            "label": {"$eq": metadata_filter}
        },
        k=1000
    )

    for result in results:
        print(result)

    return results

