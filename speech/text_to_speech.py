import subprocess
import sys

from utils.config import VOICE_RATE, VOICE_VOLUME
from utils.logger import logger


class TextToSpeech:
    def __init__(self):
        """
        Each speak() call runs pyttsx3 in a completely separate
        Python process. This avoids a known pyttsx3/Windows SAPI5
        issue where pyttsx3.init() caches one engine instance per
        driver at the module level — if that cached engine's loop
        state ever gets stuck (e.g. interrupted by a Streamlit
        rerun), every future speak() call in the same process
        fails with 'run loop already started'. A fresh process
        guarantees a fresh engine every time.
        """

        logger.info("Text-to-Speech module ready.")

    def speak(self, text: str):
        """
        Convert text into speech by running pyttsx3 in an
        isolated subprocess.

        Parameters:
            text (str): The sentence to speak.
        """

        if not text or not text.strip():
            logger.warning("Empty text received for speech.")
            return

        logger.info(f"Speaking: {text}")

        script = (
            "import pyttsx3, sys;"
            "engine = pyttsx3.init();"
            f"engine.setProperty('rate', {VOICE_RATE});"
            f"engine.setProperty('volume', {VOICE_VOLUME});"
            "engine.say(sys.argv[1]);"
            "engine.runAndWait()"
        )

        try:

            subprocess.run(
                [sys.executable, "-c", script, text],
                check=False,
                capture_output=True,
            )

        except Exception as e:

            logger.error(f"TTS error: {e}")