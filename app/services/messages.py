from fastapi import Depends
from uuid import uuid4
from sqlalchemy.orm import Session
from ..models.message import Message
from ..schemas import MessageCreate
from pydantic import BaseModel
from chat_services.vector_stores.pinecone import build_retriever


# instert a new record in to the messages table in the sqlite3 database. input variables will be role, content, and conversationID
def create_message(db: Session, message: MessageCreate): #### I may need to change this input
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages_by_conversationID(db: Session, conversationID: str):
    messages = db.query(Message).filter(Message.conversationID == conversationID).all()
    return messages
    