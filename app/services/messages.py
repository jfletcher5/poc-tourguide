from fastapi import Depends
from uuid import uuid4
from sqlalchemy.orm import Session
from ..models.message import Message
from ..schemas import MessageCreate
from pydantic import BaseModel
from chat_services.vector_stores.pinecone import build_retriever

class MessageCreate(BaseModel):
    role: str
    content: str
    conversationID: str

# instert a new record in to the messages table in the sqlite3 database. input variables will be role, content, and conversationID
def create_message(message: Message, db: Session): #### I may need to change this input
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
    