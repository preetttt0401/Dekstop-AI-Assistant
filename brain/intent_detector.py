import re

from brain.command_parser import CommandParser
from utils.helpers import normalize_text

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
    EXIT,
    GENERAL_QUESTION,
    GET_TIME,
    GET_DATE,
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
            "stop",
            "terminate",
            "kill",
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
            "x",
            "leetcode",
            "netflix",
            "spotify",
            "reddit",
            "geeksforgeeks",
            "codeforces",
        }

        self.folder_names = {
            "desktop",
            "documents",
            "downloads",
            "pictures",
            "music",
            "videos",
        }

    def detect(self, text):

        original_text = text

        text = normalize_text(text)

        words = text.split()

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
        # OPEN WEBSITE
        # -------------------------

        for word in words:

            if word in self.website_names:

                return {
                    "intent": OPEN_WEBSITE,
                    "entity": word
                }

        # -------------------------
        # OPEN FOLDER
        # -------------------------

        for folder in self.folder_names:

            if folder in words:

                return {
                    "intent": OPEN_FOLDER,
                    "entity": folder
                }

        # -------------------------
        # GOOGLE SEARCH
        # -------------------------

        if (
            text.startswith("search ")
            or text.startswith("google ")
            or text.startswith("find ")
        ):

            query = re.sub(
                r"^(search|google|find)\s+",
                "",
                original_text,
                flags=re.IGNORECASE
            )

            return {
                "intent": SEARCH_GOOGLE,
                "entity": query.strip()
            }

        # -------------------------
        # CREATE FOLDER
        # -------------------------

        if "folder" in words:

            folder_name = re.sub(
                r"(?i)(create|make|new|folder|named|called|directory)",
                "",
                original_text
            ).strip()

            if folder_name:

                return {
                    "intent": CREATE_FOLDER,
                    "entity": folder_name
                }

        # -------------------------
        # CREATE FILE
        # -------------------------

        if "file" in words:

            file_name = re.sub(
                r"(?i)(create|make|new|file|named|called)",
                "",
                original_text
            ).strip()

            if file_name:

                return {
                    "intent": CREATE_FILE,
                    "entity": file_name
                }

        # -------------------------
        # SCREENSHOT
        # -------------------------

        if (
            "screenshot" in words
            or ("screen" in words and "shot" in words)
            or ("capture" in words and "screen" in words)
        ):

            return {
                "intent": TAKE_SCREENSHOT,
                "entity": None
            }

        # -------------------------
        # BATTERY STATUS
        # -------------------------

        if "battery" in words:

            return {
                "intent": BATTERY_STATUS,
                "entity": None
            }
        
        # -------------------------
        # TIME
        # -------------------------

        if (
            "time" in words
            or ("what" in words and "time" in words)
            or ("current" in words and "time" in words)
        ):

            return {
                "intent": GET_TIME,
                "entity": None
            }

        # -------------------------
        # DATE
        # -------------------------

        if (
            "date" in words
            or ("today" in words and "date" in words)
            or ("current" in words and "date" in words)
        ):

            return {
                "intent": GET_DATE,
                "entity": None
            }

        # -------------------------
        # SHUTDOWN
        # -------------------------

        if "shutdown" in words:

            return {
                "intent": SHUTDOWN_PC,
                "entity": None
            }

        # -------------------------
        # RESTART
        # -------------------------

        if "restart" in words:

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

        if "exit" in words or "quit" in words:

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