from langchain_openai import OpenAIEmbeddings
from config import get_api_key

embeddings = OpenAIEmbeddings(
    api_key = get_api_key()
)