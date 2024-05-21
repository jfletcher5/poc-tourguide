from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from services import conversations, messages, users, tours
import logging
import shutil
from datetime import datetime
from typing import Optional


# create the fastapi app
app = FastAPI()

# create class for new conversation
class NewConversation(BaseModel):
    conversationName: str
    userID: str
    tourID: str

# create class for new message
class NewMessage(BaseModel):
    conversationID: str
    role: str
    content: str

# create class for new user
class NewUser(BaseModel):
    userAuthID: str
    name: str

# create variables for get methods
conversationID = "UUID"


#----POST new conversation--------------------------------------
@app.post("/new_conversation/")
def new_conversation(newConversation: NewConversation):
    message = conversations.create_conversation(newConversation.userID, newConversation.tourID, newConversation.conversationName)
    return message



#----GET conversation name from conversationID------------------
@app.get("/get_conversation_name/")
def get_conversation_name(conversationID: str):
    message = conversations.get_conversation_name(conversationID)
    return message




#----DELETE conversation by conversationID----------------------
@app.delete("/delete_conversation/")
def delete_conversation(conversationID: str):
    conversations.delete_conversation(conversationID)
    return {"message": f"Conversation {conversationID} deleted successfully"}


#----GET all conversations by userID----------------------------
@app.get("/get_conversations_by_userID/", description="Get all conversations by userID", name='get conversations by userID')
def get_conversations_by_userID(userID: str):
    message = conversations.get_conversations_by_userID(userID)
    return message



# post request to add a new message to a converstation. app will submit the message prompt from the user and the conversationID
@app.post("/new_message/")
def new_message(newMessage: NewMessage):
    message = messages.create_message(newMessage.role, newMessage.content, newMessage.conversationID)
    return message




# create get request to get all messages in a conversation. app will submit the conversationID
@app.get("/get_messages_by_conversationID/")
def get_messages_by_conversationID(conversationID: str):
    message = messages.get_messages_by_conversationID(conversationID)
    return message










