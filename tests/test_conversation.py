from brain.conversation import Conversation

conversation = Conversation()

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    answer = conversation.ask(question)

    print("\nBuddy :", answer)