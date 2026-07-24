from assistant import DesktopAssistant


def main():

    assistant = DesktopAssistant()

    print("=" * 50)
    print("Desktop AI Assistant Started")
    print("=" * 50)

    while True:

        assistant.listen_once()


if __name__ == "__main__":
    main()