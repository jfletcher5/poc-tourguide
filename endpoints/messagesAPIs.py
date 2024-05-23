from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from services import messages


router = APIRouter()

# create class for new message
class NewMessage(BaseModel):
    conversationID: str
    role: str
    content: str

# post request to add a new message to a converstation. app will submit the message prompt from the user and the conversationID
@router.post("/new_message/")
def new_message(newMessage: NewMessage):
    message = messages.create_message(newMessage.role, newMessage.content, newMessage.conversationID)
    return message


# create get request to get all messages in a conversation. app will submit the conversationID
@router.get("/get_messages_by_conversationID/")
def get_messages_by_conversationID(conversationID: str):
    message = messages.get_messages_by_conversationID(conversationID)
    return message

# create a post request to search pinecone for similar messages
@router.post("/search_pinecone/")
def search_pinecone(sourceID: str, input: str):
    input = input
    streaming = False

    pdf = sourceID

    chat_args = ChatArgs(
        conversation_id="123",
        pdf_id=sourceID,
        streaming=streaming,
        metadata={
            "conversation_id": "123",
            "user_id": "user",
            "pdf_id": sourceID,
        },
    )

    chat = build_chat(chat_args)

    if not chat:
        return "Chat not yet implemented!"

    if streaming:
        return Response(
            stream_with_context(chat.stream(input)), mimetype="text/event-stream"
        )
    else:
        return jsonify({"role": "assistant", "content": chat.run(input)})