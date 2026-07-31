import os

from utils.logger import logger


class FileController:

    def __init__(self):

        logger.info("File Controller initialized.")

        self.extensions = {

            "python": ".py",
            "text": ".txt",
            "txt": ".txt",
            "html": ".html",
            "css": ".css",
            "javascript": ".js",
            "js": ".js",
            "json": ".json",
            "markdown": ".md",
            "md": ".md",
            "csv": ".csv",
            "xml": ".xml",
        }

        home = os.path.expanduser("~")

        self.common_folders = {

            "desktop": os.path.join(home, "Desktop"),

            "downloads": os.path.join(home, "Downloads"),

            "documents": os.path.join(home, "Documents"),

            "pictures": os.path.join(home, "Pictures"),

            "music": os.path.join(home, "Music"),

            "videos": os.path.join(home, "Videos"),

        }

    # ------------------------------------------------

    def create_folder(self, folder_name):

        try:

            folder_name = folder_name.strip()

            if os.path.isabs(folder_name):

                folder_path = folder_name

            else:

                # Default to creating inside Desktop instead of
                # wherever the script happens to be running from.
                folder_path = os.path.join(
                    self.common_folders["desktop"], folder_name
                )

            os.makedirs(folder_path, exist_ok=True)

            logger.info(f"Folder created: {folder_path}")

            return True

        except Exception as e:

            logger.error(e)

            return False

    # ------------------------------------------------

    def open_known_folder(self, folder_name):

        try:

            folder_name = folder_name.lower().strip()

            if folder_name in self.common_folders:

                os.startfile(self.common_folders[folder_name])

                return True

            if os.path.exists(folder_name):

                os.startfile(folder_name)

                return True

            return False

        except Exception as e:

            logger.error(e)

            return False

    # ------------------------------------------------

    def create_file(self, file_name):

        try:

            words = file_name.split()

            extension = ""

            if words:

                first = words[0].lower()

                if first in self.extensions:

                    extension = self.extensions[first]

                    words = words[1:]

            file_name = " ".join(words).strip()

            if not file_name:

                file_name = "new_file"

            if extension and not file_name.endswith(extension):

                file_name += extension

            folder = os.path.dirname(file_name)

            if folder:

                os.makedirs(folder, exist_ok=True)

            with open(file_name, "a", encoding="utf-8"):
                pass

            logger.info(f"Created file: {file_name}")

            return True

        except Exception as e:

            logger.error(e)

            return False