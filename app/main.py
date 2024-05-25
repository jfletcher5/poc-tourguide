from fastapi import FastAPI
from .api import conversationAPIs, messagesAPIs, tourAPIs
from .db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(conversationAPIs.router, prefix="/api")
# app.include_router(users_api.router, prefix="/api")
app.include_router(tourAPIs.router, prefix="/api")
app.include_router(messagesAPIs.router, prefix="/api")


#when this file is run I want to call the function create_embeddings_for_pdf with "testpdf", "bostonfacts.pdf"

# if __name__ == "__main__":
    
#     #create_embeddings_for_pdf("newsource", "bostonfacts.pdf")

#     pass


