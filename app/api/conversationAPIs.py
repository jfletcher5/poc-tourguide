from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.conversations import create_conversation
# from ..schemas import Conversation
from app.models import Conversation
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
@router.post("/new_conversation/", description="Create a new conversation", name='new conversation', tags=["Conversations"])
def new_conversation(newConversation: NewConversation, db: Session = Depends(get_db)):
    message = create_conversation(db, newConversation)
    return message

#----GET conversations by userID--------------------------------------
@router.get("/get_conversations/{userID}", description="Get conversations by userID", name='get conversations by user', tags=["Conversations"])
def get_conversations(userID: str, db: Session = Depends(get_db)):
    conversations = db.query(Conversation).filter(Conversation.userID == userID).all()
    return conversations

#----GET conversations by tourID--------------------------------------
@router.get("/get_conversations_by_tourID/{tourID}", description="Get conversations by tourID", name='get conversations by tour', tags=["Conversations"])
def get_conversations_by_tourID(tourID: str, db: Session = Depends(get_db)):
    conversations = db.query(Conversation).filter(Conversation.tourID == tourID).all()
    return conversations

#----GET conversation by tourID and userID--------------------------------------
@router.get("/get_conversation/{tourID}/{userID}", description="Get conversation by tourID and userID", name='get conversation by tour and user', tags=["Conversations"])
def get_conversation(tourID: str, userID: str, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.tourID == tourID, Conversation.userID == userID).first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

#----DELETE conversation by conversationID--------------------------------------
@router.delete("/delete_conversation/{conversationID}", description="Delete conversation by conversationID", name='delete conversation by id', tags=["Conversations"])
def delete_conversation(conversationID: str, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.conversationID == conversationID).first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    db.delete(conversation)
    db.commit()
    return conversation




