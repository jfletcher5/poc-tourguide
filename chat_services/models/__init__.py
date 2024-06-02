from pydantic import BaseModel
from typing import Optional


class Metadata(BaseModel, extra='allow'):
    conversation_id: str
    user_id: str
    tourID: str


class ChatArgs(BaseModel, extra='allow'):
    conversation_id: str = "test"
    file_path: str = "./tours/Boston Common - Wikipedia.pdf"
    tourID: str = "24352fcc-cecd-45e0-821d-105437274172"
    metadata: Metadata = {
        "conversation_id": "test",
        "user_id": "123",
        "tourID": "24352fcc-cecd-45e0-821d-105437274172"
    }
    streaming: bool = False
    k: Optional[int] = 10
    score_threshold: Optional[float] = 0.8

    