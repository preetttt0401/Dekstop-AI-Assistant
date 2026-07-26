from brain.intent_detector import IntentDetector

detector = IntentDetector()

commands = [

    # -------------------------
    # Open Applications
    # -------------------------

    "open calculator",
    "launch paint",
    "start notepad",
    "run command prompt",
    "create python file hello",
    "create html file index",
    "create css file style",
    "create javascript file app",
    "create json file config",
    "create markdown file README",

    # -------------------------
    # Open Websites
    # -------------------------

    "open github",
    "open leetcode",
    "open netflix",
    "open spotify",
    "open reddit",
    "open linkedin",
    "open instagram",
    "open geeksforgeeks",
    "open codeforces",

    # -------------------------
    # Google Search
    # -------------------------

    "search python decorators",
    "search best gaming laptop",
    "google virat kohli",
    "find machine learning roadmap",

    # -------------------------
    # Folder
    # -------------------------

    "create folder Projects",
    "make folder AI",
    "new folder Desktop Assistant",

    # -------------------------
    # System Commands
    # -------------------------

    "shutdown my pc",
    "restart computer",
    "lock laptop",
    "exit assistant",
    
    "create file notes.txt",
    "create file hello.py",
    "create file README.md",
    "create file config.json",
    "open downloads",
    "open desktop",
    "open documents",
    "open pictures",
    "open music",
    "open videos",
    "take screenshot",
    "capture screen",
    "close calculator",
    "close paint",
    "close notepad",
    "close command prompt",
    "close explorer",
    "what time is it",
    "current time",
    "tell me the time",

    "today date",
    "what is today's date",
    "current date",

    # -------------------------
    # General Conversation
    # -------------------------

    "what is artificial intelligence",
    "who is virat kohli",
]

for cmd in commands:

    print(cmd)
    print(detector.detect(cmd))
    print("-" * 60)