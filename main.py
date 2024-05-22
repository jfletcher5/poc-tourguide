from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from services import conversations, messages, users, tours
from endpoints import conversationAPIs, messagesAPIs, userAPIs, tourAPIs
import logging
import shutil
from datetime import datetime
from typing import Optional
from fastapi.responses import FileResponse
from services.create_embeddings import create_embeddings_for_pdf


# create the fastapi app
app = FastAPI()


app.include_router(tourAPIs.router, tags=["Tours"], prefix="/tours")
app.include_router(conversationAPIs.router, tags=["Conversations"], prefix="/conversations")
app.include_router(messagesAPIs.router, tags=["Messages"], prefix="/messages")
app.include_router(userAPIs.router, tags=["Users"], prefix="/users")


create_embeddings_for_pdf("testpdf", "bostonfacts.pdf")