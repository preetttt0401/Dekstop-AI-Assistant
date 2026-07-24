from automation.app_controller import AppController
from speech.text_to_speech import TextToSpeech
from utils.constants import OPEN_APP, GENERAL_QUESTION


class CommandRouter:

    def __init__(self):

        self.app_controller = AppController()
        self.tts = TextToSpeech()

    def execute(self, result):

        intent = result["intent"]
        entity = result["entity"]

        if intent == OPEN_APP:

            success = self.app_controller.open_app(entity)

            if success:
                self.tts.speak(f"Opening {entity}")
            else:
                self.tts.speak("Sorry, I couldn't open that application.")

            return

        if intent == GENERAL_QUESTION:

            self.tts.speak(
                "My AI module is under development."
            )
            