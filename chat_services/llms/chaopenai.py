from langchain_openai import ChatOpenAI

def build_llm(chat_args):
    return ChatOpenAI(streaming=chat_args.streaming, model_name="gpt-4") # TODO: I may want to move the model name to a configuration somewhere