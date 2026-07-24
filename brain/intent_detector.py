import re
from utils.helpers import normalize_text
from automation.app_registry import APPS
from utils.constants import OPEN_APP, GENERAL_QUESTION
from brain.command_parser import CommandParser


class IntentDetector:
    """
    Detects the user's intent from text.
    """

    def __init__(self):
        self.open_words = [
            "open",
            "start",
            "launch",
            "run"
        ]
        self.command_parser = CommandParser()

    def clean_text(self, text: str) -> str:
        """
        Lowercase and remove punctuation.
        """

        text = text.lower()

        text = re.sub(r"[^\w\s]", "", text)

        return text.strip()

    def detect(self, text: str):

        text = normalize_text(text)

        words = text.split()

        # ---------- OPEN APP ----------

        for word in self.open_words:

            if word in words:

                app = self.command_parser.parse(text)

                if app:

                    return {
                        "intent": OPEN_APP,
                        "entity": app
                    }

        # ---------- GENERAL ----------

        return {
            "intent": GENERAL_QUESTION,
            "entity": None
        }