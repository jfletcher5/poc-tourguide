from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..services.tours import create_tour
from ..schemas import TourCreate, Tour
from pydantic import BaseModel

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
@router.post("/new_tour/", response_model=list[Tour], description="Create a new tour", name='new tour')
def new_tour(newTour: NewTour, db: Session = Depends(get_db)):
    message = create_tour(db, NewTour)
    return message
