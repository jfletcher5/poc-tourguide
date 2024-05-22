# Description: This file contains the code to create embeddings from a file and store them in a pinecone vector store

import pinecone
import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import Pinecone


load_dotenv()
#test path and file
file_path = ("/Users/jonfletcher/Documents/LLastMile/My Local Projects/poc_tourguide/bostonfacts.pdf")
index_name = "testindex"
pdf_id = "testpdf"


# create a function to load a file, use a text splitter, create embeddings from the docs using openai and store them in a pinecone vector store using an existing index
def create_embeddings(file_path: str, index_name: str):
    # create an embedder
    embeddings = OpenAIEmbeddings()

    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV_NAME")
    )

    vector_store = Pinecone.from_existing_index(
        os.getenv("PINECONE_INDEX_NAME"), embeddings
    )

    # create a text splitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50
    )

    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split(text_splitter)

    # create embeddings from the docs
    embeddings.create_embeddings(docs)

    # store the embeddings in the pinecone vector store
    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
            "pdf_id": pdf_id
        }

    vector_store.add_documents(docs)

    # return a message
    return "Embeddings created and stored in pinecone vector store"


create_embeddings(file_path, index_name)