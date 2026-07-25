import subprocess
import os
from automation.app_registry import APPS
from utils.logger import logger


class AppController:
    """
    Opens desktop applications using the application registry.
    """

    def __init__(self):
        logger.info("App Controller initialized.")

    def find_application(self, app_name: str):
        """
        Finds an application from its aliases.
        """

        app_name = app_name.lower().strip()

        for app, details in APPS.items():

            if app_name == app:
                return details

            if app_name in details["aliases"]:
                return details

        return None

    def open_app(self, app_name: str):
        """
        Opens an application.
        """

        app = self.find_application(app_name)

        if app is None:
            logger.warning(f"Unknown application: {app_name}")
            return False

        try:

            command = app["command"]

            # Windows URI (Settings etc.)
            if command.startswith("ms-"):
                os.startfile(command)

            else:
                subprocess.Popen(command)

            logger.info(f"{app_name} opened successfully.")

            return True

        except Exception as e:

            logger.error(e)

            return False
        
        def close_app(self, app_name: str):
            """
            Closes an application using taskkill.
            """

            app = self.find_application(app_name)

            if app is None:
                logger.warning(f"Unknown application: {app_name}")
                return False

            try:

                command = app["command"]

                if command.endswith(".exe"):

                    subprocess.run(
                        ["taskkill", "/F", "/IM", command],
                        capture_output=True
                    )

                    logger.info(f"{app_name} closed successfully.")
                    return True

                return False

            except Exception as e:

                logger.error(e)

                return False