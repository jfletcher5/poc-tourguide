from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from langchain_core.chat_history import BaseChatMessageHistory


class SQLChatMessageHistory():
    conversation_id: str
    connection_string: str = "sqlite:///chat_history.db"



def build_memory(chat_args):    
    return RunnableWithMessageHistory(
        chat_memory=SQLChatMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    pass