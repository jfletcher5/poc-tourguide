from fastapi import FastAPI
from endpoints import conversationAPIs, messagesAPIs, userAPIs, tourAPIs
from fastapi.responses import FileResponse
from services.create_embeddings import create_embeddings_for_pdf


# create the fastapi app
app = FastAPI()


app.include_router(tourAPIs.router, tags=["Tours"], prefix="/tours")
app.include_router(conversationAPIs.router, tags=["Conversations"], prefix="/conversations")
app.include_router(messagesAPIs.router, tags=["Messages"], prefix="/messages")
app.include_router(userAPIs.router, tags=["Users"], prefix="/users")

#when this file is run I want to call the function create_embeddings_for_pdf with "testpdf", "bostonfacts.pdf"

if __name__ == "__main__":
    
    #create_embeddings_for_pdf("newsource", "bostonfacts.pdf")

    pass


