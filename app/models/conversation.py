import datetime, uuid
from sqlalchemy import Column, DateTime, Integer, String
from app.db import Base



class Conversation(Base):
    
    __tablename__ = "conversations"

    conversationID = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    create_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    tourID = Column(String)
    conversationName = Column(String)
    userID = Column(String)

    def __repr__(self):
        return f"<Conversation(conversationID={self.conversationID}, create_date={self.create_date}, tourID={self.tourID}, conversationName={self.conversationName}, userID={self.userID})>"

