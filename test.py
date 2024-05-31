from chat_services import build_chat
from chat_services.models import ChatArgs
# from chat_services.vector_stores.pinecone import build_retriever
from chat_services.llms import build_llm

def test_chat_creation():
    # Define test chat arguments
    chat_args = ChatArgs(
        conversation_id="560dde47-8079-4dc2-b902-70ec11a74b44",
        file_path="./tours/Boston Common - Wikipedia.pdf",
        tourID="24352fcc-cecd-45e0-821d-105437274172", #this tour is for the boston common wiki 24352fcc-cecd-45e0-821d-105437274172
        metadata={
            "conversation_id": "560dde47-8079-4dc2-b902-70ec11a74b44",
            "user_id": "123",
            "tourID": "24352fcc-cecd-45e0-821d-105437274172"
        },
        streaming=False,
        k=3 # returns number of docs from vstore
    )

    # test the llm
    llm = build_llm(chat_args)
    result = llm.invoke("What is the capital of the United States?")
    print(f"LLM response is {result}")


if __name__ == "__main__":
    test_chat_creation()

# things I can do here: 
# 1. pass in chat args which include the pieces of information needed to build the chat
# 2. build the retriever and query documents with an input prompt
# 3. use build_llm to build the llm from llm module and use it to generate a response with a prompt. use invoke to call the llm directly