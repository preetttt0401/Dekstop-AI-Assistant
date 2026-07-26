import webbrowser
import urllib.parse

from utils.logger import logger


POPULAR_WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "leetcode": "https://leetcode.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://x.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "wikipedia": "https://www.wikipedia.org",
    "stackoverflow": "https://stackoverflow.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "codeforces": "https://codeforces.com",
    "codechef": "https://www.codechef.com",
    "hackerrank": "https://www.hackerrank.com",
    "canva": "https://www.canva.com",
    "figma": "https://www.figma.com",
    "notion": "https://www.notion.so",
    "discord": "https://discord.com",
    "whatsapp": "https://web.whatsapp.com",
    "drive": "https://drive.google.com",
    "maps": "https://maps.google.com",
}


class BrowserController:

    def __init__(self):
        logger.info("Browser Controller initialized.")

    def open_website(self, website_name):

        website_name = website_name.lower().strip()

        if website_name in POPULAR_WEBSITES:
            url = POPULAR_WEBSITES[website_name]
        else:
            url = f"https://www.{website_name}.com"

        try:
            webbrowser.open(url)
            logger.info(f"Opened website: {url}")
            return True

        except Exception as e:
            logger.error(e)
            return False

    def google_search(self, query):

        try:

            query = urllib.parse.quote(query)

            url = f"https://www.google.com/search?q={query}"

            webbrowser.open(url)

            logger.info(f"Google Search: {query}")

            return True

        except Exception as e:

            logger.error(e)

            return False