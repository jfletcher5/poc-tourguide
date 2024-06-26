# Description: This file contains the code to create embeddings from a file and store them in a pinecone vector store

from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from chat_services.vector_stores.pinecone import vector_store
from chat_services.embeddings.openai import embeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone


def create_embeddings_for_pdf(label: str, file_path: str):
    text_splitter = SemanticChunker(
        OpenAIEmbeddings(),
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