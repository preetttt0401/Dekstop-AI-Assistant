from brain.intent_detector import IntentDetector

detector = IntentDetector()

commands = [
    "open calculator",
    "open github",
    "shutdown my pc",
    "restart computer",
    "lock laptop",
    "exit assistant",
    "close calculator",
    "close notepad",
    "close paint",
]

for cmd in commands:
    print(cmd)
    print(detector.detect(cmd))
    print("-" * 40)