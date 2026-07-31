from dotenv import load_dotenv
import os

# Load variables from .env into the environment
load_dotenv()

# ==========================
# LLM Configuration
# ==========================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LLM_MODEL = "gemini-flash-latest"

# ==========================
# Text-to-Speech Configuration
# ==========================
VOICE_RATE = 170
VOICE_VOLUME = 1.0

# ==========================
# Speech-to-Text Configuration
# ==========================
WHISPER_MODEL = "base"

# ==========================
# Audio Recording
# ==========================
SAMPLE_RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5