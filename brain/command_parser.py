import re

from automation.app_registry import APPS
from utils.helpers import BASE_FILLER_WORDS


class CommandParser:
    """
    Converts natural language into application names.
    """

    def __init__(self):

        self.extra_aliases = {

            "draw": "paint",
            "drawing": "paint",
            "painting": "paint",

            "write": "notepad",
            "notes": "notepad",

            "math": "calculator",
            "maths": "calculator",
            "calculate": "calculator",

            "terminal": "command prompt",
            "cmd": "command prompt",

            "explorer": "explorer",
            "files": "explorer",

            "powershell": "powershell",
            "power shell": "powershell",
        }

        self.ignore_words = BASE_FILLER_WORDS | {
            "to",
            "for",
            "open",
            "launch",
            "start",
            "run",
            "use",
            "show",
            "opening",
            "app",
            "application",
        }

    def clean_text(self, text: str) -> str:
        """
        Removes punctuation and unnecessary words.
        """

        text = text.lower()

        text = re.sub(r"[^\w\s]", "", text)

        words = []

        for word in text.split():

            if word not in self.ignore_words:
                words.append(word)

        return " ".join(words)

    def parse(self, text: str):
        """
        Returns the canonical application name if found.
        """

        cleaned = self.clean_text(text)

        # Match application names

        for app, details in APPS.items():

            if app in cleaned:
                return app

            for alias in details["aliases"]:

                if alias in cleaned:
                    return app

        # Match extra aliases

        for alias, app in self.extra_aliases.items():

            if alias in cleaned:
                return app

        return None