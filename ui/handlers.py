def add_user_message(state, text):

    state.messages.append(
        {
            "role": "user",
            "content": text
        }
    )


def add_bot_message(state, text):

    state.messages.append(
        {
            "role": "assistant",
            "content": text
        }
    )