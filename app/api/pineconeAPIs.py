from fastapi import APIRouter
from ..db import SessionLocal
from ..services.pinecone_service import delete_vectors_by_metadata
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DefaultValues(BaseModel):
    metadata_filter: str = "c6fc4dda-19aa-4b97-a5ea-fd163da0eefc"

#----delete vectors by filter criteria--------------------------------------
@router.delete("/delete_vectors_by_metadata", description="Delete vectors by metadata", name='delete vectors by metadata', tags=["Pinecone"])
def delete_vectors_by_metadata_route(indexInfo: DefaultValues):
    results = delete_vectors_by_metadata(indexInfo.metadata_filter)
    return results

    