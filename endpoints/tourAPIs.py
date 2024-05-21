from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import tours

router = APIRouter()

class NewTour(BaseModel):
    tourName: str
    tourDescription: str
    tourCategory: str

#----POST new tour--------------------------------------
@router.post("/new_tour/")
def new_tour(newTour: NewTour):
    message = tours.create_tour(newTour.tourName, newTour.tourDescription, newTour.tourCategory)
    return message
