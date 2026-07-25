from automation.app_controller import AppController
from automation.browser_controller import BrowserController
from automation.file_controller import FileController

from brain.conversation import Conversation

from speech.text_to_speech import TextToSpeech

from utils.constants import (
    OPEN_APP,
    OPEN_WEBSITE,
    CREATE_FOLDER,
    GENERAL_QUESTION
)


class CommandRouter:

    def __init__(self):

        self.tts = TextToSpeech()

        self.app_controller = AppController()
        self.browser_controller = BrowserController()
        self.file_controller = FileController()

        self.conversation = Conversation()

    def execute(self, result):

        intent = result["intent"]
        entity = result["entity"]

        # ----------------------------
        # OPEN APPLICATION
        # ----------------------------

        if intent == OPEN_APP:

            success = self.app_controller.open_app(entity)

            if success:
                self.tts.speak(f"Opening {entity}")
            else:
                self.tts.speak("Sorry, I couldn't open that application.")

            return

        # ----------------------------
        # OPEN WEBSITE
        # ----------------------------

        elif intent == OPEN_WEBSITE:

            success = self.browser_controller.open_website(entity)

            if success:
                self.tts.speak(f"Opening {entity}")
            else:
                self.tts.speak("Sorry, I couldn't open that website.")

            return

        # ----------------------------
        # CREATE FOLDER
        # ----------------------------

        elif intent == CREATE_FOLDER:

            success = self.file_controller.create_folder(entity)

            if success:
                self.tts.speak("Folder created successfully.")
            else:
                self.tts.speak("Unable to create the folder.")

            return

        # ----------------------------
        # AI Conversation
        # ----------------------------

        elif intent == GENERAL_QUESTION:

            answer = self.conversation.ask(entity)

            print(f"\nAssistant : {answer}")

            self.tts.speak(answer)

            return