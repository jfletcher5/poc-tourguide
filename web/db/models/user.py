import datetime
import uuid
from sqlalchemy import Column, DateTime, Integer, String
from web.db.models.database import Base



class User(Base):
    
    __tablename__ = "users"

    #userID with a default of a random uuid
    userID = Column(String, primary_key=True, index=True)
    userName = Column(String)
    email = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.utcnow)
