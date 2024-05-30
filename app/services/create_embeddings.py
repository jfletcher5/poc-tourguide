# Description: This file contains the code to create embeddings from a file and store them in a pinecone vector store

import pinecone
import os
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import Pinecone
from chat_services.vector_stores.pinecone import vector_store
from chat_services.embeddings.openai import embeddings


def create_embeddings_for_pdf(label: str, file_path: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )

    loader = PyPDFLoader(file_path)
    
    docs = loader.load_and_split(text_splitter)

    # print the number of characters in each doc in docs
    for doc in docs:
        print(len(doc.page_content))


    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "filename": file_path,
            "label": label
        }

    vector_store.add_documents(docs)