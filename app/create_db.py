from db import engine, Base
from models import user, conversation, message, tours

# Create the database tables
Base.metadata.create_all(bind=engine)