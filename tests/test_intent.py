from brain.intent_detector import IntentDetector

detector = IntentDetector()

tests = [

    "Open calculator",

    "Please open calculator",

    "Can you open calculator",

    "I want to draw",

    "I want to paint",

    "I want to write",

    "Run terminal",

    "Start command prompt",

    "What is gravity?",

    "Who made Python?"
]

for sentence in tests:

    print(sentence)

    print(detector.detect(sentence))

    print("-" * 40)