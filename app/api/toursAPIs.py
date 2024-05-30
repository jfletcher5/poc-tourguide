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
@router.post("/new_tour/", description="Create a new tour record in the database", name='new tour', tags=["Tours"])
def new_tour(newTour: NewTour, db: Session = Depends(get_db)):
    message = create_tour(db, newTour)
    return message

#----POST new tour with pdf--------------------------------------
@router.post("/new_tour_with_pdf/", description="Create a new tour record in the database and create embeddings for a pdf file", name='new tour with pdf', tags=["Tours"])
def new_tour_with_pdf(tourID: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # save file in ./tours
    with open(f"./tours/{file.filename}", "wb") as f:
        f.write(file.file.read())
    
    file_path = f"./tours/{file.filename}"
    message2 = create_embeddings_with_pdf(tourID, file_path)
    return message2

#----GET all tours--------------------------------------
@router.get("/get_all_tours/", description="Get all tours", name='get all tours', tags=["Tours"])
def get_all_tours(db: Session = Depends(get_db)):
    tours = db.query(Tour).all()
    return tours

#----GET tours by tourID--------------------------------------
@router.get("/get_tour/{tourID}", description="Get tour by tourID", name='get tour by id', tags=["Tours"])
def get_tour(tourID: str, db: Session = Depends(get_db)):
    tour = db.query(Tour).filter(Tour.tourID == tourID).first()
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return tour

#----delete tours by tourID--------------------------------------
@router.delete("/delete_tour/{tourID}", description="Delete tour by tourID", name='delete tour by id', tags=["Tours"])
def delete_tour(tourID: str, db: Session = Depends(get_db)):
    tour = db.query(Tour).filter(Tour.tourID == tourID).first()
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    db.delete(tour)
    db.commit()
    return tour





