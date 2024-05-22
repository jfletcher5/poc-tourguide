from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import tours

router = APIRouter()

class NewTour(BaseModel):
    tourName: str
    tourDescription: str
    tourCategory: str

#----POST new tour--------------------------------------
#include a file upload url
@router.post("/new_tour/")
def new_tour(newTour: NewTour):
    message = tours.create_tour(newTour.tourName, newTour.tourDescription, newTour.tourCategory)
    return message

#----GET tour name from tourID------------------
@router.get("/get_tour_name/")
def get_tour_name(tourID: str):
    message = tours.get_tour_name(tourID)
    return message

#----GET tour ID by name----------------------------
@router.get("/get_tourID_by_name/")
def get_tourIDs_by_name(tourName: str):
    message = tours.get_tourIDs_by_name(tourName)
    return message

#----DELETE tour by tourID----------------------
@router.delete("/delete_tour/")
def delete_tour(tourID: str):
    tours.delete_tour(tourID)
    return {"message": f"Tour {tourID} deleted successfully"}