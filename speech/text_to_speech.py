import pyttsx3

from utils.config import VOICE_RATE, VOICE_VOLUME
from utils.logger import logger


class TextToSpeech:
    def __init__(self):
        """
        Initialize the Text-to-Speech engine.
        This runs only once when the assistant starts.
        """
        self.engine = pyttsx3.init()

        # Configure voice properties
        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

        logger.info("Text-to-Speech engine initialized.")

    def speak(self, text: str):
        """
        Convert text into speech.

        Parameters:
            text (str): The sentence to speak.
        """
        if not text.strip():
            logger.warning("Empty text received for speech.")
            return

        logger.info(f"Speaking: {text}")

        self.engine.say(text)
        self.engine.runAndWait()