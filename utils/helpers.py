import re


def normalize_text(text: str) -> str:
    """
    Normalize user input before intent detection.
    """

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    filler_words = [
        "please",
        "can",
        "could",
        "would",
        "you",
        "the",
        "a",
        "an",
        "me"
    ]

    words = []

    for word in text.split():

        if word not in filler_words:

            words.append(word)

    return " ".join(words)