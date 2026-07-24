from brain.command_router import CommandRouter
from brain.intent_detector import IntentDetector
from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech
from utils.constants import OPEN_APP, GENERAL_QUESTION
from utils.logger import logger


class DesktopAssistant:

    def __init__(self):

        logger.info("Starting Desktop Assistant...")

        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        self.intent_detector = IntentDetector()
        self.router = CommandRouter()

    def process_text(self, text: str):

        logger.info(f"User: {text}")

        result = self.intent_detector.detect(text)

        self.router.execute(result)
        
    def listen_once(self):
        """
        Listen once from microphone.
        """

        text = self.stt.listen()

        if not text:
            return

        print(f"\nYou : {text}")

        self.process_text(text)