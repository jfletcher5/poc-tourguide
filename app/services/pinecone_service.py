from fastapi import Depends
from uuid import uuid4
import os
from chat_services.vector_stores.pinecone import vector_store
from chat_services.embeddings import openai
from pinecone import Pinecone

# def method to clear all vectors in the pinecone index filtered by metadata. make the default input PINECONE_INDEX_NAME but allow it to be changed
def delete_vectors_by_index(metadata_filter: str):
    
    
    # if vector_store.get_pinecone_index(metadata_filter) returns exception, show the error details
    try:   
        index = vector_store.get_pinecone_index(metadata_filter)
    except Exception as e:
        return str(e)


    # delete all vectors in the index
    vector_store.delete(
        delete_all=True,
        )

    return f'all vectors in {metadata_filter} deleted'

