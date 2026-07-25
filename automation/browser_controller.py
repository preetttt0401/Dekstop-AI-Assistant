import webbrowser

from utils.logger import logger


WEBSITES = {

    "google": "https://www.google.com",

    "youtube": "https://www.youtube.com",

    "gmail": "https://mail.google.com",

    "github": "https://github.com",

    "chatgpt": "https://chat.openai.com",

    "wikipedia": "https://www.wikipedia.org",

    "stackoverflow": "https://stackoverflow.com",

    "amazon": "https://www.amazon.in",

    "linkedin": "https://www.linkedin.com",

    "instagram": "https://www.instagram.com",

    "facebook": "https://www.facebook.com",

    "twitter": "https://x.com"
}


class BrowserController:

    """
    Opens websites in the default browser.
    """

    def __init__(self):

        logger.info("Browser Controller initialized.")

    def open_website(self, website_name):

        website_name = website_name.lower().strip()

        if website_name not in WEBSITES:

            logger.warning(f"Unknown website: {website_name}")

            return False

        webbrowser.open(WEBSITES[website_name])

        logger.info(f"{website_name} opened successfully.")

        return True