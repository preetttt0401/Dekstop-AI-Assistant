import ctypes
import os

from utils.logger import logger


class SystemController:
    """
    Handles Windows system operations.
    """

    def __init__(self):
        logger.info("System Controller initialized.")

    def shutdown(self):
        try:
            os.system("shutdown /s /t 1")
            logger.info("Shutdown command executed.")
            return True
        except Exception as e:
            logger.error(e)
            return False

    def restart(self):
        try:
            os.system("shutdown /r /t 1")
            logger.info("Restart command executed.")
            return True
        except Exception as e:
            logger.error(e)
            return False

    def lock(self):
        try:
            ctypes.windll.user32.LockWorkStation()
            logger.info("PC locked.")
            return True
        except Exception as e:
            logger.error(e)
            return False