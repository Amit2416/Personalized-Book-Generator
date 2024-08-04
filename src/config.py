import os
from dotenv import load_dotenv
import anthropic
from openai import OpenAI

# Load .env file
load_dotenv()

def get_api_key(key_name):
    api_key = os.getenv(key_name)
    if not api_key:
        api_key = input(f"Enter your {key_name}: ")
    return api_key

ANTHROPIC_API_KEY = get_api_key("ANTHROPIC_API_KEY")
OPENAI_API_KEY = get_api_key("OPENAI_API_KEY")

anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)