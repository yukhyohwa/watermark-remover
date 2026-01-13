import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = "gemini-2.5-flash-latest"

# Processing Configuration
MAX_TEXT_CHUNK_SIZE = 15000

# Audio Configuration
DEFAULT_LANGUAGE = 'zh-tw'
