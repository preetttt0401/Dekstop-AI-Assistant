from brain.command_router import CommandRouter
from brain.intent_detector import IntentDetector
from brain.conversation import Conversation

from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech

from utils.constants import GENERAL_QUESTION
from utils.logger import logger


class DesktopAssistant:

    def __init__(self):

        logger.info("Starting Desktop Assistant...")

        self.stt = SpeechToText()
        self.tts = TextToSpeech()

        self.intent_detector = IntentDetector()
        self.router = CommandRouter()
        self.conversation = Conversation()

    # -------------------------------------------------

    def process_text(self, text: str):

        logger.info(f"User : {text}")

        result = self.intent_detector.detect(text)

        # ------------------------
        # AI Conversation
        # ------------------------

        if result["intent"] == GENERAL_QUESTION:

            answer = self.conversation.ask(result["entity"])

            self.tts.speak(answer)

            return answer

        # ------------------------
        # Automation Commands
        # ------------------------

        self.router.execute(result)

        intent = result["intent"]

        if intent == "OPEN_APP":
            return f"Opening {result['entity']}."

        elif intent == "CLOSE_APP":
            return f"Closing {result['entity']}."

        elif intent == "OPEN_WEBSITE":
            return f"Opening {result['entity']}."

        elif intent == "SEARCH_GOOGLE":
            return f"Searching Google for {result['entity']}."

        elif intent == "CREATE_FOLDER":
            return "Folder created successfully."

        elif intent == "CREATE_FILE":
            return "File created successfully."

        elif intent == "OPEN_FOLDER":
            return f"Opening {result['entity']}."

        elif intent == "BATTERY_STATUS":
            return self.router.system_controller.battery_status()

        elif intent == "GET_TIME":
            return self.router.system_controller.current_time()

        elif intent == "GET_DATE":
            return self.router.system_controller.current_date()

        elif intent == "TAKE_SCREENSHOT":

            path = self.router.system_controller.take_screenshot()

            if path:
                return f"Screenshot saved at\n{path}"

            return "Unable to capture screenshot."

        elif intent == "LOCK_PC":
            return "Locking your computer."

        elif intent == "RESTART_PC":
            return "Restarting your computer."

        elif intent == "SHUTDOWN_PC":
            return "Shutting down your computer."

        elif intent == "EXIT":
            return "Goodbye."

        return "Done."

    # -------------------------------------------------

    def listen_once(self):

        text = self.stt.listen()

        if not text:

            return None, None

        print(f"\nYou : {text}")

        answer = self.process_text(text)

        return text, answer