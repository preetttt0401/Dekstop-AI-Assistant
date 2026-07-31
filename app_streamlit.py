import streamlit as st

from assistant import DesktopAssistant
from utils.logger import logger


# ======================================================
# Page Config
# ======================================================

st.set_page_config(
    page_title="Desktop AI Assistant",
    page_icon="🤖",
    layout="centered",
)


# ======================================================
# Load the assistant once (heavy models: Whisper + TTS)
# ======================================================

@st.cache_resource(show_spinner="Loading Desktop AI Assistant...")
def load_assistant():

    logger.info("Loading DesktopAssistant for Streamlit UI...")

    return DesktopAssistant()


assistant = load_assistant()


# ======================================================
# Session State
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "confirm_power_action" not in st.session_state:
    st.session_state.confirm_power_action = False


def add_message(role, text):

    st.session_state.messages.append({"role": role, "content": text})


def run_command(text):
    """
    Sends text to the assistant and safely handles the EXIT intent,
    which raises SystemExit inside CommandRouter.
    """

    add_message("user", text)

    try:

        answer = assistant.process_text(text)

    except SystemExit:

        answer = "Goodbye. (Assistant session ended — reload the page to start again.)"

    add_message("assistant", answer)


# ======================================================
# Sidebar — Quick Actions
# ======================================================

with st.sidebar:

    st.header("⚙️ Quick Actions")

    st.subheader("Info")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔋 Battery", use_container_width=True):
            run_command("battery status")

        if st.button("📅 Date", use_container_width=True):
            run_command("what is the date")

    with col2:

        if st.button("🕒 Time", use_container_width=True):
            run_command("what is the time")

        if st.button("📸 Screenshot", use_container_width=True):
            run_command("take a screenshot")

    st.subheader("Apps")

    col3, col4 = st.columns(2)

    with col3:

        if st.button("📝 Notepad", use_container_width=True):
            run_command("open notepad")

        if st.button("🧮 Calculator", use_container_width=True):
            run_command("open calculator")

    with col4:

        if st.button("🎨 Paint", use_container_width=True):
            run_command("open paint")

        if st.button("📁 Explorer", use_container_width=True):
            run_command("open explorer")

    st.subheader("Folders")

    col5, col6 = st.columns(2)

    with col5:

        if st.button("🖥️ Desktop", use_container_width=True):
            run_command("open desktop folder")

    with col6:

        if st.button("⬇️ Downloads", use_container_width=True):
            run_command("open downloads folder")

    st.divider()

    st.subheader("⚠️ Power Actions")

    st.session_state.confirm_power_action = st.checkbox(
        "I understand these affect my real PC"
    )

    col7, col8, col9 = st.columns(3)

    with col7:

        if st.button("🔒 Lock", use_container_width=True,
                      disabled=not st.session_state.confirm_power_action):
            run_command("lock my pc")

    with col8:

        if st.button("🔄 Restart", use_container_width=True,
                      disabled=not st.session_state.confirm_power_action):
            run_command("restart my pc")

    with col9:

        if st.button("⏻ Shutdown", use_container_width=True,
                      disabled=not st.session_state.confirm_power_action):
            run_command("shutdown my pc")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ======================================================
# Main Chat Area
# ======================================================

st.title("🤖 Desktop AI Assistant")
st.caption("Type a command, or use the microphone button below.")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# ------------------------------------------------------
# Voice input
# ------------------------------------------------------

col_mic, col_note = st.columns([1, 4])

with col_mic:

    listen_clicked = st.button("🎤 Speak (5s)")

with col_note:

    st.caption("Records from this machine's microphone for 5 seconds.")

if listen_clicked:

    with st.spinner("Listening..."):

        text, answer = assistant.listen_once()

    if text:

        add_message("user", text)
        add_message("assistant", answer)
        st.rerun()

    else:

        st.warning("No speech detected. Please try again.")


# ------------------------------------------------------
# Text input
# ------------------------------------------------------

typed_text = st.chat_input("Type a command or question...")

if typed_text:

    run_command(typed_text)
    st.rerun()