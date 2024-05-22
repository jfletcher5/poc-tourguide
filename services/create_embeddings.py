# Description: This file contains the code to create embeddings from a file and store them in a pinecone vector store

import pinecone
import os
from dotenv import load_dotenv
import langchain
from langchain import TextSplitter, Embedder

load_dotenv()

# create a function to load a file, use a text splitter, create embeddings from the docs using openai and store them in a pinecone vector store using an existing index
def create_embeddings(file_path: str, index_name: str):
    # create a connection to the pinecone vector store
    pinecone.init
    pinecone.connect(api_key=os.getenv)
    index = pinecone.Index(index_name)

    # load the file
    with open(file_path, 'r') as file:
        docs = file.readlines()

    # create a text splitter
    text_splitter = TextSplitter()
    text_splitter.split(docs)

    # create an embedder
    embedder = Embedder()
    embedder.embed(text_splitter.sentences)

    # store the embeddings in the pinecone vector store
    index.upsert(text_splitter.sentences, ids=text_splitter.ids)

    # return a message
    return "Embeddings created and stored in pinecone vector store"
