from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import conversations

router = APIRouter()

# create class for new conversation
class NewConversation(BaseModel):
    conversationName: str
    userID: str
    tourID: str

#----POST new conversation--------------------------------------
@router.post("/new_conversation/")
def new_conversation(newConversation: NewConversation):
    message = conversations.create_conversation(newConversation.userID, newConversation.tourID, newConversation.conversationName)
    return message



#----GET conversation name from conversationID------------------
@router.get("/get_conversation_name/")
def get_conversation_name(conversationID: str):
    message = conversations.get_conversation_name(conversationID)
    return message


#----DELETE conversation by conversationID----------------------
@router.delete("/delete_conversation/")
def delete_conversation(conversationID: str):
    conversations.delete_conversation(conversationID)
    return {"message": f"Conversation {conversationID} deleted successfully"}


#----GET all conversations by userID----------------------------
@router.get("/get_conversations_by_userID/", description="Get all conversations by userID", name='get conversations by userID')
def get_conversations_by_userID(userID: str):
    message = conversations.get_conversations_by_userID(userID)
    return message