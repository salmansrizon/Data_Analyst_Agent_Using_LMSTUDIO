import os
from dotenv import load_dotenv
import yaml
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

def load_llm_config():
    """
    Load LLM configuration from environment variables.
    """
    return {
        "model_name": os.getenv("LLM_MODEL_NAME", "gemma-3-1b-it"),
        "base_url": os.getenv("LLM_BASE_URL"),
        "api_key": os.getenv("LLM_API_KEY"),
        "temperature": float(os.getenv("LLM_TEMPERATURE", 0.7)),
        "max_tokens": int(os.getenv("LLM_MAX_TOKENS", 500)),
        "timeout": int(os.getenv("LLM_TIMEOUT", 60))
    }

def load_db_config():
    """
    Load database configuration from environment variables.
    """
    return {
        "type": "postgresql",
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT")),
        "username": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "database_name": os.getenv("DB_NAME")
    }