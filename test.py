from chat_services import build_chat
from chat_services.models import ChatArgs

def test_chat_creation():
    # Define test chat arguments
    chat_args = ChatArgs(
        conversation_id="560dde47-8079-4dc2-b902-70ec11a74b44",
        file_path="./tours/Boston Common - Wikipedia.pdf",
        tourID="24352fcc-cecd-45e0-821d-105437274172",
        metadata={
            "conversation_id": "560dde47-8079-4dc2-b902-70ec11a74b44",
            "user_id": "123",
            "tourID": "24352fcc-cecd-45e0-821d-105437274172"
        },
        streaming=False
    )

    # Build chat
    chat = build_chat(chat_args)

    # Simulate starting a chat (this will depend on how your chat method is implemented)
    chat.invoke('hi')

    # Add assertions or checks as needed
    print("Chat built and started successfully.")

if __name__ == "__main__":
    test_chat_creation()