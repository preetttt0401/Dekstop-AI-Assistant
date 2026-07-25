from langchain_google_genai import ChatGoogleGenerativeAI

from utils.config import GEMINI_API_KEY, LLM_MODEL
from utils.logger import logger

logger.info("Initializing Gemini model...")

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.4
)

logger.info("Gemini model initialized successfully.")