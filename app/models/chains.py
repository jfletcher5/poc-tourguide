import datetime, uuid
from sqlalchemy import Column, DateTime, Integer, String
from app.db import Base



class Chain(Base):
    
    __tablename__ = "chain"

    chainID = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    conversationID = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    tourID = Column(String)
    chainName = Column(String)
    userID = Column(String)

    def __repr__(self):
        return f"<Chain(chainID={self.chainID}, conversationID={self.conversationID}, create_date={self.create_date}, tourID={self.tourID}, conversationName={self.chainName}, userID={self.userID})>"