from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import users

router = APIRouter()


# create class for new user
class NewUser(BaseModel):
    userAuthID: str
    name: str