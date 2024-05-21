from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import tours

router = APIRouter()

