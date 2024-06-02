from chat_services import build_chat
from chat_services.vector_stores.pinecone import build_retriever
from chat_services.models import ChatArgs
from chat_services.llms import build_llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.chains import create_retrieval_chain, create_history_aware_retriever

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

contextualized_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
    )

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualized_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)


system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id: SQLChatMessageHistory(
        session_id=session_id, connection_string=db_path
    ),
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

conversational_rag_chain.invoke(
    {"input": "what did I say a five messages ago?"},
    config={
        "configurable": {"session_id": session_id}
    },  # constructs a key "abc123" in `store`.
)["answer"]

from langchain_core.messages import AIMessage

message_history = chat_message_history.messages

for message in message_history:
    if isinstance(message, AIMessage):
        prefix = "AI"
    else:
        prefix = "User"

    print(f"{prefix}: {message.content}\n")