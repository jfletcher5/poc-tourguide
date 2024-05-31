from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel

from langchain.schema import BaseChatMessageHistory


class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str



def build_memory(chat_args):    
#     return ConversationBufferMemory(
#         chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
#         return_messages=True,
#         memory_key="chat_history",
#         output_key="answer"
#     )
    pass