from sqlalchemy.orm import Session
from ..models.message import Message
from ..schemas import MessageCreate
from chat_services.vector_stores.pinecone import build_retriever
from langchain.schema.messages import AIMessage, HumanMessage, SystemMessage


# instert a new record in to the messages table in the sqlite3 database. input variables will be role, content, and conversationID
def create_message(db: Session, message: MessageCreate): #### I may need to change this input
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages_by_conversationID(db: Session, conversationID: str) -> AIMessage | HumanMessage | SystemMessage:
    messages = db.query(Message).filter(Message.conversationID == conversationID).order_by(Message.create_date.desc())
    return [message.as_lc_message() for message in messages]
    