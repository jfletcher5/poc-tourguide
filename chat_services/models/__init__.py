from pydantic import BaseModel


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
