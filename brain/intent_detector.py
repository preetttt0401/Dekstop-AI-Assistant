import re

from brain.command_parser import CommandParser
from utils.helpers import normalize_text

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


class IntentDetector:

    def __init__(self):

        self.command_parser = CommandParser()

        self.open_words = [
            "open",
            "launch",
            "start",
            "run",
            "visit",
            "go"
        ]
        
        self.close_words = [
            "close",
            "terminate",
            "kill",
            "stop"
            ]

        self.website_names = {
            "google",
            "youtube",
            "gmail",
            "github",
            "chatgpt",
            "wikipedia",
            "stackoverflow",
            "amazon",
            "linkedin",
            "instagram",
            "facebook",
            "twitter",
            "x"
        }

        self.shutdown_words = {
            "shutdown",
            "shut",
            "poweroff",
            "power",
            "turn"
        }

        self.restart_words = {
            "restart",
            "reboot"
        }

        self.lock_words = {
            "lock"
        }

        self.exit_words = {
            "exit",
            "quit",
            "close",
            "bye"
        }

    def detect(self, text):

        original_text = text

        text = normalize_text(text)

        words = text.split()

        # -------------------------
        # OPEN APP
        # -------------------------

        for word in self.open_words:

            if word in words:

                app = self.command_parser.parse(original_text)

                if app:

                    return {
                        "intent": OPEN_APP,
                        "entity": app
                    }
        # -------------------------
        # CLOSE APP
        # -------------------------

        for word in self.close_words:

            if word in words:

                app = self.command_parser.parse(original_text)

                if app:

                    return {
                        "intent": CLOSE_APP,
                        "entity": app
                    }

        # -------------------------
        # OPEN WEBSITE
        # -------------------------

        for i, word in enumerate(words):

            if word in self.open_words:

                if i + 1 < len(words):

                    next_word = words[i + 1]

                    app = self.command_parser.parse(next_word)

                    if app is None:

                        return {
                            "intent": OPEN_WEBSITE,
                            "entity": next_word
                        }

        # -------------------------
        # CREATE FOLDER
        # -------------------------

        if (
            ("folder" in words or "directory" in words)
            and (
                "create" in words
                or "make" in words
                or "new" in words
            )
        ):

            folder_name = original_text

            folder_name = re.sub(
                r"(?i)(create|make|new|folder|directory|named|called)",
                "",
                folder_name
            )

            folder_name = folder_name.strip()

            if folder_name:

                return {
                    "intent": CREATE_FOLDER,
                    "entity": folder_name
                }

        # -------------------------
        # SHUTDOWN
        # -------------------------

        if (
            "shutdown" in words
            or ("shut" in words and "down" in words)
            or ("turn" in words and "off" in words)
            or ("power" in words and "off" in words)
        ):

            return {
                "intent": SHUTDOWN_PC,
                "entity": None
            }

        # -------------------------
        # RESTART
        # -------------------------

        if any(word in words for word in self.restart_words):

            return {
                "intent": RESTART_PC,
                "entity": None
            }

        # -------------------------
        # LOCK
        # -------------------------

        if "lock" in words:

            return {
                "intent": LOCK_PC,
                "entity": None
            }

        # -------------------------
        # EXIT
        # -------------------------

        if any(word in words for word in self.exit_words):

            return {
                "intent": EXIT,
                "entity": None
            }

        # -------------------------
        # GENERAL QUESTION
        # -------------------------

        return {
            "intent": GENERAL_QUESTION,
            "entity": original_text
        }