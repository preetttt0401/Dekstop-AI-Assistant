from automation.app_controller import AppController
from automation.browser_controller import BrowserController
from automation.file_controller import FileController
from automation.system_controller import SystemController
from automation.system_controller import SystemController
from brain.conversation import Conversation

from speech.text_to_speech import TextToSpeech

from utils.constants import (
    OPEN_APP,
    OPEN_WEBSITE,
    CREATE_FOLDER,
    SHUTDOWN_PC,
    RESTART_PC,
    LOCK_PC,
    EXIT,
    GENERAL_QUESTION,
    CLOSE_APP
)


class CommandRouter:

    def __init__(self):

        self.tts = TextToSpeech()

        self.app_controller = AppController()
        self.browser_controller = BrowserController()
        self.file_controller = FileController()
        self.system_controller = SystemController()

        self.conversation = Conversation()
        self.system_controller = SystemController()

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
        # CLOSE APPLICATION
        # ----------------------------

        elif intent == CLOSE_APP:

            success = self.app_controller.close_app(entity)

            if success:
                self.tts.speak(f"Closing {entity}")
            else:
                self.tts.speak("Sorry, I couldn't close that application.")

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
        # SHUTDOWN
        # ----------------------------

        elif intent == SHUTDOWN_PC:

            self.tts.speak("Shutting down the computer.")

            self.system_controller.shutdown()

            return

        # ----------------------------
        # RESTART
        # ----------------------------

        elif intent == RESTART_PC:

            self.tts.speak("Restarting the computer.")

            self.system_controller.restart()

            return

        # ----------------------------
        # LOCK
        # ----------------------------

        elif intent == LOCK_PC:

            self.tts.speak("Locking the computer.")

            self.system_controller.lock()

            return

        # ----------------------------
        # EXIT ASSISTANT
        # ----------------------------

        elif intent == EXIT:

            self.tts.speak("Goodbye!")

            raise SystemExit
        # ----------------------------
        # SYSTEM COMMANDS
        # ----------------------------

        elif intent == SHUTDOWN_PC:

            success = self.system_controller.shutdown()

            if success:
                self.tts.speak("Shutting down your computer.")
            else:
                self.tts.speak("Unable to shut down the computer.")

            return

        elif intent == RESTART_PC:

            success = self.system_controller.restart()

            if success:
                self.tts.speak("Restarting your computer.")
            else:
                self.tts.speak("Unable to restart the computer.")

            return

        elif intent == LOCK_PC:

            success = self.system_controller.lock()

            if success:
                self.tts.speak("Locking your computer.")
            else:
                self.tts.speak("Unable to lock the computer.")

            return

        # ----------------------------
        # AI Conversation
        # ----------------------------

        elif intent == GENERAL_QUESTION:

            answer = self.conversation.ask(entity)

            print(f"\nAssistant : {answer}")

            self.tts.speak(answer)

            return