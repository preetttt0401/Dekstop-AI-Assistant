import re

# Shared base filler words used across intent parsing.
# App-specific parsers can extend this set with their own extra words.
BASE_FILLER_WORDS = {
    "please",
    "can",
    "could",
    "would",
    "you",
    "the",
    "a",
    "an",
    "me",
    "my",
    "will",
}


def normalize_text(text: str) -> str:
    """
    Normalize user input before intent detection.
    """

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    words = []

    for word in text.split():

        if word not in BASE_FILLER_WORDS:

            words.append(word)

    return " ".join(words)