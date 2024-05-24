import datetime, uuid
from sqlalchemy import Column, DateTime, Integer, String
from db.database import Base



class Message(Base):
    
    __tablename__ = "messages"

    messageID = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    role = Column(String)
    content = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
    conversationID = Column(String, foreign_key=True)

    def __repr__(self):
        return f"<Message(messageID={self.messageID}, role={self.role}, content={self.content}, create_date={self.create_date}, conversationID={self.conversationID})>"
