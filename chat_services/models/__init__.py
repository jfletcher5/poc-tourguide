from pydantic import BaseModel
from typing import Optional


class Metadata(BaseModel, extra='allow'):
    conversation_id: str
    user_id: str
    tourID: str


class ChatArgs(BaseModel, extra='allow'):
    conversation_id: str
    file_path: str
    tourID: str
    metadata: Metadata
    streaming: bool
    k: Optional[int] = None
    score_threshold: Optional[float] = None
