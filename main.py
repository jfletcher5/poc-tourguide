from fastapi import FastAPI
from endpoints import conversationAPIs, messagesAPIs, userAPIs, tourAPIs
from fastapi.responses import FileResponse
from services.create_embeddings import create_embeddings_for_pdf
from web.db.database import engine, Base


# create the fastapi app
app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)




#when this file is run I want to call the function create_embeddings_for_pdf with "testpdf", "bostonfacts.pdf"

# if __name__ == "__main__":
    
#     #create_embeddings_for_pdf("newsource", "bostonfacts.pdf")

#     pass


