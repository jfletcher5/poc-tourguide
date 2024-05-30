from langchain_community.chat_models import ChatOpenAI
from chat_services.models import ChatArgs
from chat_services.vector_stores.pinecone import build_retriever
from chat_services.llms.chaopenai import build_llm
from chat_services.memories.sql_memory import build_memory
from chat_services.chains.retrieval import StreamingConversationalRetrievalChain

def build_chat(chat_args: ChatArgs):
    retriever = build_retriever(chat_args) # this works
    llm = build_llm(chat_args) # this works
    condense_question_llm=ChatOpenAI(streaming=False)
    memory = build_memory(chat_args)

    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        condense_question_llm=condense_question_llm,
        memory=memory,
        retriever=retriever
    ) 