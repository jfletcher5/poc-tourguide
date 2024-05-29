from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.conversations import create_conversation
from ..schemas import Conversation
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class NewConversation(BaseModel):
    tourID: str
    conversationName: str
    userID: str

#----POST new conversation--------------------------------------
@router.post("/new_conversation/", description="Create a new conversation", name='new conversation')
def new_conversation(newConversation: NewConversation, db: Session = Depends(get_db)):
    message = create_conversation(db, newConversation)
    return message


