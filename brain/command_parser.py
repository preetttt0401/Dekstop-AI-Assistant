import re

from automation.app_registry import APPS


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
        }

        self.ignore_words = {
            "please",
            "can",
            "could",
            "would",
            "you",
            "me",
            "my",
            "the",
            "a",
            "an",
            "to",
            "for",
            "open",
            "launch",
            "start",
            "run",
            "use",
            "show"
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

        cleaned = self.clean_text(text)

        # Search registry aliases

        for app, details in APPS.items():

            if app in cleaned:
                return app

            for alias in details["aliases"]:

                if alias in cleaned:
                    return app

        # Search extra aliases

        for word, app in self.extra_aliases.items():

            if word in cleaned:
                return app

        return None