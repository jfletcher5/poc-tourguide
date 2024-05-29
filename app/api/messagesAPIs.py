from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.messages import create_message
# from ..schemas import Message
from pydantic import BaseModel
from app.models import Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create class for new message
class NewMessage(BaseModel):
    role: str
    content: str
    conversationID: str
    

# post request to add a new message to a converstation. app will submit the message prompt from the user and the conversationID
@router.post("/new_message/", description="Create a new message", name='new message in conversation')
def new_message(newMessage: NewMessage, db: Session = Depends(get_db)):
    message = create_message(db, newMessage)
    return message

# get messages by conversationID
@router.get("/get_messages/{conversationID}", description="Get messages by conversationID", name='get messages by conversation')
def get_messages(conversationID: str, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(Message.conversationID == conversationID).all()
    return messages

# delete message by messageID
@router.delete("/delete_message/{messageID}", description="Delete message by messageID", name='delete message')
def delete_message(messageID: str, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.messageID == messageID).first()
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(message)
    db.commit()
    return message