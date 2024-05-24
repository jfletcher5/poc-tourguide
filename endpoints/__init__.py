# endpoints/__init__.py
from fastapi import APIRouter
from . import conversationAPIs, messagesAPIs, userAPIs, tourAPIs

api_router = APIRouter()

api_router.include_router(tourAPIs.router, tags=["Tours"], prefix="/tours")
api_router.include_router(conversationAPIs.router, tags=["Conversations"], prefix="/conversations")
api_router.include_router(messagesAPIs.router, tags=["Messages"], prefix="/messages")
api_router.include_router(userAPIs.router, tags=["Users"], prefix="/users")