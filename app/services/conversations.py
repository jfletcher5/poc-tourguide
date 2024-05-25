from fastapi import Depends
from uuid import uuid4
from sqlalchemy.orm import Session
from ..models.conversation import Conversation
from ..schemas import ConversationCreate
from pydantic import BaseModel


# instert a new record in to the conversations table in the sqlite3 database. input variables will be userID, tourID, and conversationName
def create_conversation(db: Session, conversation: Conversation): #### I may need to change this input
    db_conversation = Conversation(**conversation.model_dump())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

