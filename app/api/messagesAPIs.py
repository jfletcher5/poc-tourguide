from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.messages import create_message
from ..schemas import Message
from pydantic import BaseModel

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
@router.post("/new_message/", description="Create a new message", name='new message')
def new_message(newMessage: NewMessage, db: Session = Depends(get_db)):
    message = create_message(db, newMessage)
    return message
