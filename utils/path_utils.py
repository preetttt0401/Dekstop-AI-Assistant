import os


def get_desktop():
    return os.path.join(os.path.expanduser("~"), "Desktop")


def get_documents():
    return os.path.join(os.path.expanduser("~"), "Documents")


def get_downloads():
    return os.path.join(os.path.expanduser("~"), "Downloads")


def get_pictures():
    return os.path.join(os.path.expanduser("~"), "Pictures")


def get_music():
    return os.path.join(os.path.expanduser("~"), "Music")


def get_videos():
    return os.path.join(os.path.expanduser("~"), "Videos")