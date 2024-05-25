from fastapi import FastAPI
from app.api import conversationAPIs, toursAPIs, messagesAPIs
from app.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(conversationAPIs.router, prefix="/api/conversations")
# app.include_router(users_api.router, prefix="/api/users")
app.include_router(toursAPIs.router, prefix="/api/tours")
app.include_router(messagesAPIs.router, prefix="/api/messages")