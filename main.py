from fastapi import FastAPI
from app.api import conversationAPIs, toursAPIs, messagesAPIs, pineconeAPIs, chainsAPIs
from app.db import engine, Base

# Import models to ensure they are registered with SQLAlchemy
from app.models import user, conversation, message, tours

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(toursAPIs.router, prefix="/api/tours")
app.include_router(conversationAPIs.router, prefix="/conversations")
# app.include_router(usersAPIs.router, prefix="/api/users")
app.include_router(messagesAPIs.router, prefix="/messages")
app.include_router(pineconeAPIs.router, prefix="/pinecone")
app.include_router(chainsAPIs.router, prefix="/chains")