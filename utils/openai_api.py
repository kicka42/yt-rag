import os
import sys
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("OPENAI_API_KEY not found in environment variables.")
    sys.exit(1)

client_openai = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

def connect_openai():
    try:
        result = client_openai.models.get_model(model)
        return result
    except Exception as e:
        return str(e)
