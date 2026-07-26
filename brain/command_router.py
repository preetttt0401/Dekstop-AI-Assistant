from automation.app_controller import AppController
from automation.browser_controller import BrowserController
from automation.file_controller import FileController
from automation.system_controller import SystemController

from brain.conversation import Conversation

from speech.text_to_speech import TextToSpeech

from utils.constants import (
    OPEN_APP,
    CLOSE_APP,
    OPEN_WEBSITE,
    OPEN_FOLDER,
    SEARCH_GOOGLE,
    CREATE_FOLDER,
    CREATE_FILE,
    SHUTDOWN_PC,
    RESTART_PC,
    LOCK_PC,
    TAKE_SCREENSHOT,
    BATTERY_STATUS,
    GET_TIME,
    GET_DATE,
    EXIT,
    GENERAL_QUESTION,
)


class CommandRouter:

    def __init__(self):

        self.tts = TextToSpeech()

        self.app_controller = AppController()
        self.browser_controller = BrowserController()
        self.file_controller = FileController()
        self.system_controller = SystemController()

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
        # CLOSE APPLICATION
        # ----------------------------

        elif intent == CLOSE_APP:

            success = self.app_controller.close_app(entity)

            if success:
                self.tts.speak(f"Closing {entity}")
            else:
                self.tts.speak("Unable to close the application.")

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
        # GOOGLE SEARCH
        # ----------------------------

        elif intent == SEARCH_GOOGLE:

            success = self.browser_controller.google_search(entity)

            if success:
                self.tts.speak(f"Searching Google for {entity}")
            else:
                self.tts.speak("Unable to search Google.")

            return

        # ----------------------------
        # OPEN FOLDER
        # ----------------------------

        elif intent == OPEN_FOLDER:

            success = self.file_controller.open_known_folder(entity)

            if success:
                self.tts.speak(f"Opening {entity}")
            else:
                self.tts.speak("Unable to open the folder.")

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
        # CREATE FILE
        # ----------------------------

        elif intent == CREATE_FILE:

            success = self.file_controller.create_file(entity)

            if success:
                self.tts.speak("File created successfully.")
            else:
                self.tts.speak("Unable to create the file.")

            return

        # ----------------------------
        # SHUTDOWN PC
        # ----------------------------

        elif intent == SHUTDOWN_PC:

            self.tts.speak("Shutting down your computer.")

            self.system_controller.shutdown_pc()

            return

        # ----------------------------
        # RESTART PC
        # ----------------------------

        elif intent == RESTART_PC:

            self.tts.speak("Restarting your computer.")

            self.system_controller.restart_pc()

            return

        # ----------------------------
        # LOCK PC
        # ----------------------------

        elif intent == LOCK_PC:

            self.tts.speak("Locking your computer.")

            self.system_controller.lock_pc()

            return

        # ----------------------------
        # TAKE SCREENSHOT
        # ----------------------------

        elif intent == TAKE_SCREENSHOT:

            path = self.system_controller.take_screenshot()

            if path:

                print(f"\nSaved at : {path}")

                self.tts.speak("Screenshot captured successfully.")

            else:

                self.tts.speak("Unable to capture screenshot.")

            return

        # ----------------------------
        # BATTERY STATUS
        # ----------------------------

        elif intent == BATTERY_STATUS:

            message = self.system_controller.battery_status()

            print(f"\nAssistant : {message}")

            self.tts.speak(message)

            return
        
        # ----------------------------
        # CURRENT TIME
        # ----------------------------

        elif intent == GET_TIME:

            message = self.system_controller.current_time()

            print(f"\nAssistant : {message}")

            self.tts.speak(message)

            return

        # ----------------------------
        # CURRENT DATE
        # ----------------------------

        elif intent == GET_DATE:

            message = self.system_controller.current_date()

            print(f"\nAssistant : {message}")

            self.tts.speak(message)

            return

        # ----------------------------
        # EXIT
        # ----------------------------

        elif intent == EXIT:

            self.tts.speak("Goodbye.")

            raise SystemExit

        # ----------------------------
        # AI CONVERSATION
        # ----------------------------

        elif intent == GENERAL_QUESTION:

            answer = self.conversation.ask(entity)

            print(f"\nAssistant : {answer}")

            self.tts.speak(answer)

            return