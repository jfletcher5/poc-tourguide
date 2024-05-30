from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory, BaseChatMessageHistory
from app.services.messages import (
    get_messages_by_conversationID as get_messages_by_conversation_id,
    create_message as add_message_to_conversation
)

class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages (self):
        return get_messages_by_conversation_id(self.conversation_id)
    
    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )
    
    def clear(self):
        pass


def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )