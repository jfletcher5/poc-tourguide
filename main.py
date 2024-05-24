# app/main.py
from fastapi import FastAPI
from web.db.database import engine, Base
from .endpoints import api_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(api_router)


#when this file is run I want to call the function create_embeddings_for_pdf with "testpdf", "bostonfacts.pdf"

# if __name__ == "__main__":
    
#     #create_embeddings_for_pdf("newsource", "bostonfacts.pdf")

#     pass


