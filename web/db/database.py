# database.py
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from databases import Database
from typing import AsyncGenerator

DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Create a Base class for declarative class definitions
Base = declarative_base()

# Define a sample model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Create the database tables
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

# Alternative async database setup using databases package
database = Database(DATABASE_URL)
