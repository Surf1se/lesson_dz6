import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value


API_KEY = get_env_variable("API_KEY")
TOKEN = get_env_variable("TOKEN")
USERNAME = get_env_variable("USERNAME")
PASSWORD = get_env_variable("PASSWORD")