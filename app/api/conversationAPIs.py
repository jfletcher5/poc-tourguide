from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.conversations import create_conversation
from ..schemas import ConversationCreate, Conversation
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#----POST new conversation--------------------------------------
@router.post("/new_conversation/", response_model=list[Conversation], description="Create a new conversation", name='new conversation')
def new_conversation(newConversation: Conversation, db: Session = Depends(get_db)):
    message = create_conversation(db, Conversation)
    return message


