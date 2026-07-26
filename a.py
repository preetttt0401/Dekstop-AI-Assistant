import streamlit as st
from assistant import DesktopAssistant

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Desktop Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# SESSION STATE
# =====================================

if "assistant" not in st.session_state:
    st.session_state.assistant = DesktopAssistant()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "status" not in st.session_state:
    st.session_state.status = "🟢 Ready"

assistant = st.session_state.assistant

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

html,body,.stApp{
    background:#0f172a;
}

.block-container{
    padding-top:1rem;
}

.main-title{

    font-size:42px;
    font-weight:700;
    color:white;
    text-align:center;

}

.sub-title{

    color:#94a3b8;
    text-align:center;
    font-size:17px;
    margin-bottom:20px;

}

.status-box{

    background:#1e293b;
    color:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-weight:bold;
    margin-bottom:20px;

}

.user-msg{

    background:#2563eb;
    color:white;
    padding:14px;
    border-radius:12px;
    margin-top:10px;
    margin-bottom:10px;

}

.bot-msg{

    background:#1e293b;
    color:white;
    padding:14px;
    border-radius:12px;
    margin-top:10px;
    margin-bottom:10px;

}

.bigbutton button{

    width:100%;
    height:65px;
    font-size:22px;
    border-radius:15px;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🤖 AI Desktop Assistant")

    st.write("---")

    st.success(st.session_state.status)

    st.write("---")

    st.subheader("Quick Actions")

    screenshot = st.button("📸 Screenshot")

    battery = st.button("🔋 Battery")

    current_time = st.button("🕒 Current Time")

    current_date = st.button("📅 Current Date")

    st.write("---")

    st.subheader("Conversation")

    st.write(f"Messages : {len(st.session_state.messages)}")

    st.write("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()

# =====================================
# HEADER
# =====================================

st.markdown(
    "<div class='main-title'>🤖 AI Desktop Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Voice Powered Desktop Automation Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='status-box'>{st.session_state.status}</div>",
    unsafe_allow_html=True
)

# =====================================
# CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    if message["role"]=="user":

        st.markdown(
            f"<div class='user-msg'><b>You</b><br>{message['content']}</div>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"<div class='bot-msg'><b>Assistant</b><br>{message['content']}</div>",
            unsafe_allow_html=True
        )

st.write("")
st.write("")

# =====================================
# MIC BUTTON
# =====================================

col1,col2,col3=st.columns([1,2,1])

with col2:

    mic=st.button(
        "🎤 Start Listening",
        use_container_width=True
    )

st.write("")
# =====================================
# QUICK ACTIONS
# =====================================

if screenshot:

    st.session_state.status = "📸 Capturing Screenshot..."

    answer = assistant.process_text("take screenshot")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.status = "🟢 Ready"

    st.rerun()


if battery:

    st.session_state.status = "🔋 Checking Battery..."

    answer = assistant.process_text("battery status")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.status = "🟢 Ready"

    st.rerun()


if current_time:

    st.session_state.status = "🕒 Getting Time..."

    answer = assistant.process_text("current time")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.status = "🟢 Ready"

    st.rerun()


if current_date:

    st.session_state.status = "📅 Getting Date..."

    answer = assistant.process_text("current date")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.status = "🟢 Ready"

    st.rerun()


# =====================================
# MICROPHONE
# =====================================

if mic:

    st.session_state.status = "🎤 Listening..."

    with st.spinner("Listening..."):

        text, answer = assistant.listen_once()

    if text:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": text
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    st.session_state.status = "🟢 Ready"

    st.rerun()


# =====================================
# TEXT CHAT
# =====================================

prompt = st.chat_input("Type a message...")


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.session_state.status = "🟡 Thinking..."

    with st.spinner("Thinking..."):

        answer = assistant.process_text(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.status = "🟢 Ready"

    st.rerun()