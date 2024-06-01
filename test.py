from chat_services import build_chat
from chat_services.vector_stores.pinecone import build_retriever
from chat_services.models import ChatArgs
from chat_services.llms import build_llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.chains import create_retrieval_chain

# Define test chat arguments
chat_args = ChatArgs(
    conversation_id="560dde47-8079-4dc2-b902-70ec11a74b44",
    file_path="./tours/Boston Common - Wikipedia.pdf",
    tourID="24352fcc-cecd-45e0-821d-105437274172", #this tour is for the boston common wiki 24352fcc-cecd-45e0-821d-105437274172
    metadata={
        "conversation_id": "560dde47-8079-4dc2-b902-70ec11a74b44",
        "user_id": "123",
        "tourID": "24352fcc-cecd-45e0-821d-105437274172"
    },
    streaming=False,
    k=10, # returns number of docs from vstore
    score_threshold=0.8
)
retriever = build_retriever(chat_args=chat_args)
llm = build_llm(chat_args=chat_args)
session_id = "123" #conversation id will go here
db_path = "sqlite:///sqlite_test.db" #path to db in env variables

chat_message_history = SQLChatMessageHistory(
        session_id=session_id, connection_string=db_path
    )
llm = build_llm(chat_args=chat_args)
retriever = build_retriever(chat_args=chat_args)

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "ONLY Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise. If the retrieved context is not relevant for the question "
    "respond with 'I don't know'."
    "\n\n"
    "{context}"
    )

#-----------------TESTS-----------------#

def test_chat_with_history():

    # system_prompt = (
    # "You are an assistant for question-answering tasks. "
    # "ONLY Use the following pieces of retrieved context to answer "
    # "the question. If you don't know the answer, say that you "
    # "don't know. Use three sentences maximum and keep the "
    # "answer concise. If the retrieved context is not relevant for the question "
    # "respond with 'I don't know'."
    # "\n\n"
    # )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | llm

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: SQLChatMessageHistory(
            session_id=session_id, connection_string=db_path
        ),
        input_messages_key="question",
        history_messages_key="history"
        )
    
    # This is where we configure the session id
    config = {"configurable": {"session_id": session_id}}
    
    chain_with_history.invoke({"question": "how old is the common"}, config=config)

    messages = chat_message_history.messages

    for m in messages:
        print(m.type)
        print(m.content)

def test_chat_with_rag():

    system_prompt = (
    "You are an assistant for question-answering tasks. "
    "ONLY Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise. If the retrieved context is not relevant for the question "
    "respond with 'I don't know'."
    "\n\n"
    "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
        )
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    result = rag_chain.invoke({"input": "can you tell me something fun about the boston common"})

    print(result['input'])
    print(result['answer'])


if __name__ == "__main__":
    method = input("Choose history or rag: ")
    if method == "history":
        test_chat_with_history()
    elif method == "rag":
        test_chat_with_rag()
    else:
        print("Invalid choice")

    

# things I can do here: 
# 1. pass in chat args which include the pieces of information needed to build the chat
# 2. build the retriever and query documents with an input prompt
# 3. use build_llm to build the llm from llm module and use it to generate a response with a prompt. use invoke to call the llm directly
# 