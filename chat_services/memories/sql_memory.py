from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from langchain_core.chat_history import BaseChatMessageHistory
import os

PROJECT_ID = os.getenv('GCLOUD_PROJECT_ID')

class FirestoreChatMessageHistory():
    conversation_id: str
    collection: str = "chat_history"



def build_memory(chat_args):    
    return RunnableWithMessageHistory(
        chat_memory=FirestoreChatMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    pass