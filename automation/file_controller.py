import os

from utils.logger import logger


class FileController:
    """
    Handles file and folder operations.
    """

    def __init__(self):
        logger.info("File Controller initialized.")

    def create_folder(self, folder_path):
        """
        Creates a folder if it doesn't already exist.
        """

        try:

            os.makedirs(folder_path, exist_ok=True)

            logger.info(f"Folder created: {folder_path}")

            return True

        except Exception as e:

            logger.error(e)

            return False

    def open_folder(self, folder_path):
        """
        Opens a folder using Windows File Explorer.
        """

        try:

            if not os.path.exists(folder_path):

                logger.warning(f"Folder not found: {folder_path}")

                return False

            os.startfile(folder_path)

            logger.info(f"Opened folder: {folder_path}")

            return True

        except Exception as e:

            logger.error(e)

            return False