import os
from dotenv import load_dotenv

def init():
    # Set the API key and user from .env file
    load_dotenv()
    api_key = os.getenv('API_KEY')
    user = os.getenv('USER')
    return user, api_key
