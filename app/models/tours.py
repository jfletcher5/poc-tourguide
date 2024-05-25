import datetime, uuid
from sqlalchemy import Column, DateTime, Integer, String
from app.db import Base



class Tour(Base):
    
    __tablename__ = "tours_new"

    tourID = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    tourName = Column(String)
    tourDescription = Column(String)

    def __repr__(self):
        return f"<Pdf(tourID={self.tourID}, tourName={self.tourName}, tourDescription={self.tourDescription})>"