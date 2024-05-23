# Description: This file contains the code to create embeddings from a file and store them in a pinecone vector store

import pinecone
import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import Pinecone
from chat_services.vector_stores.pinecone import vector_store
from chat_services.embeddings.openai import embeddings


def create_embeddings_for_pdf(lookup: str, pdf_path: str):
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split(text_splitter)

    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "lookup": lookup
        }

    vector_store.add_documents(docs)