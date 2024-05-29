from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.tours import create_tour, create_embeddings_with_pdf
from ..schemas import TourCreate, Tour
from pydantic import BaseModel
from app.models import Tour
from fastapi import UploadFile, File

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class NewTour(BaseModel):
    tourName: str
    tourDescription: str
    tourCategory: str

#----POST new tour--------------------------------------
#include a file upload url
@router.post("/new_tour/", description="Create a new tour record in the database", name='new tour')
def new_tour(newTour: NewTour, db: Session = Depends(get_db)):
    message = create_tour(db, newTour)
    return message

#----POST new tour with pdf--------------------------------------
@router.post("/new_tour_with_pdf/", description="Create a new tour record in the database and create embeddings for a pdf file", name='new tour with pdf')
def new_tour_with_pdf(tourID: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # save file in ./tours
    with open(f"./tours/{file.filename}", "wb") as f:
        f.write(file.file.read())
    
    file_path = f"./tours/{file.filename}"
    message2 = create_embeddings_with_pdf(tourID, file_path)
    return message2




