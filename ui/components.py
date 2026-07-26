import streamlit as st


def render_header(status):

    st.markdown(
        "<div class='main-title'>🤖 AI Desktop Assistant</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Voice Powered Desktop Automation Assistant</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='status'>{status}</div>",
        unsafe_allow_html=True
    )


def render_chat(messages):

    for message in messages:

        if message["role"] == "user":

            st.markdown(
                f"<div class='user'><b>You</b><br>{message['content']}</div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"<div class='bot'><b>Assistant</b><br>{message['content']}</div>",
                unsafe_allow_html=True
            )