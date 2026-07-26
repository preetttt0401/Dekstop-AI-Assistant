import subprocess
import os

from automation.app_registry import APPS
from utils.logger import logger


class AppController:

    def __init__(self):

        logger.info("App Controller initialized.")

    # ------------------------------------------------

    def find_application(self, app_name):

        app_name = app_name.lower().strip()

        for app, details in APPS.items():

            if app == app_name:
                return details

            if app_name in details["aliases"]:
                return details

        return None

    # ------------------------------------------------

    def open_app(self, app_name):

        app = self.find_application(app_name)

        if app is None:
            return False

        try:

            command = app["command"]

            if command.startswith("ms-"):

                os.startfile(command)

            else:

                subprocess.Popen(command)

            logger.info(f"Opened {app_name}")

            return True

        except Exception as e:

            logger.error(e)

            return False

    # ------------------------------------------------

    def close_app(self, app_name):

        app = self.find_application(app_name)

        if app is None:

            return False

        try:

            exe = app["command"]

            exe = exe.replace(".exe", "")

            subprocess.run(

                ["taskkill", "/IM", exe + ".exe", "/F"],

                capture_output=True,

                text=True

            )

            logger.info(f"Closed {app_name}")

            return True

        except Exception as e:

            logger.error(e)

            return False