from langchain_community.chat_message_histories import SQLChatMessageHistory
from vector_stores.pinecone import vector_store, build_retriever
from models import ChatArgs

chat_message_history = SQLChatMessageHistory(
    session_id="test_session", connection_string="sqlite:///sqlite.db"
)

# chat_message_history.add_user_message("Hello")
# chat_message_history.add_ai_message("Hi")

# print(chat_message_history.messages)
chat_args = ChatArgs(
    conversation_id="test_conversation",
    tourID="2cd2b8d4-43c2-45f5-b255-2de3b312b9bd",
    user_id="test_user",
    role="user",
    message="Hello",
    file_path="test_file_path",
    metadata={"conversation_id": "test_conversation", "user_id": "test_user", "tourID": "2cd2b8d4-43c2-45f5-b255-2de3b312b9bd"},
    streaming=False
)

retriever = build_retriever(chat_args)
message = retriever.invoke("when should you not dial 911")
print(message)
