from pydantic import BaseModel
from typing import Optional, List

# Conversation Schemas
class ConversationBase(BaseModel):
    title: str
    description: Optional[str] = None

class ConversationCreate(ConversationBase):
    pass

class Conversation(ConversationBase):
    id: int

    class Config:
        orm_mode = True

# Message Schemas
class MessageBase(BaseModel):
    content: str
    conversation_id: int
    sender_id: int

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    timestamp: Optional[str] = None  # Add timestamp if you track message time

    class Config:
        orm_mode = True

# Tour Schemas
class TourBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: Optional[str] = None

class TourCreate(TourBase):
    pass

class Tour(TourBase):
    id: int

    class Config:
        orm_mode = True

class ChainBase(BaseModel):
    conversation_id: int
    message_id: int
    message_type: str
    message: str

class ChainCreate(ChainBase):
    pass

class Chain(ChainBase):
    id: int

    class Config:
        orm_mode = True

