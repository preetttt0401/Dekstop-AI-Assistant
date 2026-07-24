import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/assistant.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Create logger object
logger = logging.getLogger("DesktopAIAssistant")