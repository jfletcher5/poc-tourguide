# app/config.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite+aiosqlite:///./test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
