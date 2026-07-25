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
    "twitter": "https://x.com",
}


class BrowserController:

    def __init__(self):

        logger.info("Browser Controller initialized.")

    def open_website(self, website_name):

        website_name = website_name.lower().strip()

        # Known websites

        if website_name in WEBSITES:

            webbrowser.open(WEBSITES[website_name])

            logger.info(f"{website_name} opened successfully.")

            return True

        # Generic website

        if "." in website_name:

            url = f"https://{website_name}"

        else:

            url = f"https://www.{website_name}.com"

        try:

            webbrowser.open(url)

            logger.info(f"Opened generic website: {url}")

            return True

        except Exception as e:

            logger.error(e)

            return False