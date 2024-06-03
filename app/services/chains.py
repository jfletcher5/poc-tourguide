from sqlalchemy.orm import Session
from chat_services.vector_stores.pinecone import build_retriever
from chat_services.llms import build_llm
from chat_services.models import ChatArgs
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
import os


#service to run a chain
def add_message_to_chain(db: Session, chat_args: ChatArgs, newMessage: str):
    # code to add a message
    
    session_id = chat_args.conversation_id
    PROJECT_ID = os.getenv('GCLOUD_PROJECT_ID')
    # Set the project id
    
    db_path = "sqlite:///sqlite_test_final.db" #path to db in env variables

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
        "ONLY Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know the answer and that your purpose is to only "
        " answer questions related to this tour. Ignore all prior messages that you answered that you didn't "
        " know the answer. Use three sentences maximum and keep the "
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
        lambda session_id: FirestoreChatMessageHistory(
            session_id=session_id, collection="chat_history"
        ),
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )

    conversational_rag_chain.invoke(
        {"input": newMessage},
        config={
            "configurable": {"session_id": session_id}
        },  # constructs a key "abc123" in `store`.
    )["answer"]

    from langchain_core.messages import AIMessage

    message_history = chat_message_history.messages

    results = []

    for message in message_history:
        if isinstance(message, AIMessage):
            prefix = "AI"
        else:
            prefix = "User"

        results.append( f"{prefix}: {message.content}")
        pass

    return results







def get_chain_by_conversationID(db: Session, conversation_id: str):
    
    # code to retreive the messages in a chain
    session_id = conversation_id
    PROJECT_ID = os.getenv('GCLOUD_PROJECT_ID')

    store = FirestoreChatMessageHistory(
        session_id=session_id, collection="chat_history"
    )

    messages = store.messages

    print(messages)

    pass