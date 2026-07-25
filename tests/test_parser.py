from brain.command_parser import CommandParser

parser = CommandParser()

print("=" * 60)
print("Command Parser Test")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    command = input("\nCommand: ")

    if command.lower() == "exit":
        break

    result = parser.parse(command)

    print("Detected App:", result)