from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from pydantic import BaseModel
from app.models import Chain
from fastapi import UploadFile, File
from ..services.chains import add_message_to_chain, get_chain_by_conversationID
from chat_services.models import ChatArgs

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add_message_to_chain", tags=["Chains"])
async def create_chain_message(chat_args: ChatArgs, newMessage: str, db: Session = Depends(get_db)):
    result = add_message_to_chain(db, chat_args, newMessage)

    return result

@router.get("/get_chain_by_conversationID", tags=["Chains"])
async def get_chain_by_conversationID(conversation_id: str, db: Session = Depends(get_db)):
    result = get_chain_by_conversationID(db, conversation_id)

    return result
