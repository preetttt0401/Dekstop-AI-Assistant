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

    def parse(self, text: str):

        text = text.lower()

        # Search registry aliases first

        for app, details in APPS.items():

            if app in text:
                return app

            for alias in details["aliases"]:

                if alias in text:
                    return app

        # Search extra aliases

        for word, app in self.extra_aliases.items():

            if word in text:
                return app

        return None