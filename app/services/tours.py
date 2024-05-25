from fastapi import Depends
from uuid import uuid4
from sqlalchemy.orm import Session
from ..models.tours import Tour
from ..schemas import TourCreate
from pydantic import BaseModel
from .create_embeddings import create_embeddings_for_pdf



#----------------------------------------------------------------------------------------
# insert a new record in to the tours table in the sqlite3 database. input variables will be tourName, tourDescription, and tourCategory
def create_tour(db: Session, tour: TourCreate): #### I may need to change this input
    db_tour = Tour(**tour.model_dump())
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour

#----------------------------------------------------------------------------------------

# create service to consume a filename string and run create_embeddings_for_pdf
def create_embeddings_with_pdf(label: str, filename: str):
    
    create_embeddings_for_pdf(label, filename)

    return {"message": f"Embeddings for {filename} created successfully with a lookup of {label}"}