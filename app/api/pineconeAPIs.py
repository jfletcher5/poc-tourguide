from fastapi import APIRouter
from ..db import SessionLocal
from ..services.pinecone_service import delete_vectors_by_index, get_docs_by_query
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DefaultValues(BaseModel):
    indexName: str = "testindex"

#----delete vectors by index--------------------------------------
@router.delete("/delete_vectors_by_index", description="Delete vectors by index", name='delete vectors by index', tags=["Pinecone"])
def delete_vectors_by_metadata_route(indexInfo: DefaultValues):
    results = delete_vectors_by_index(indexInfo.indexName)
    return results

#----return list of docs by query--------------------------------------
@router.get("/get_docs_by_query", description="Get documents by query", name='get docs by query', tags=["Pinecone"])
def get_docs_by_query_api(query: str):
    results = get_docs_by_query(query)
    return results

    