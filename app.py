import streamlit as st
from chat import CustomerSupportChat
from datetime import datetime

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# CSS
# -------------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.main .block-container{
padding-top:1rem;
padding-bottom:1rem;
padding-left:2rem;
padding-right:2rem;
}

html,body,[class*="css"]{
font-family:Segoe UI;
}

.main{
background:#0f172a;
}

.title{
font-size:42px;
font-weight:700;
text-align:center;
color:white;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#94a3b8;
margin-bottom:30px;
}

.user-box{

background:#2563eb;

padding:15px;

border-radius:15px;

margin-top:15px;

margin-bottom:10px;

color:white;

}

.bot-box{

background:#1e293b;

padding:15px;

border-radius:15px;

margin-top:10px;

margin-bottom:15px;

border-left:5px solid #38bdf8;

color:white;

}

.intent{

color:#38bdf8;

font-size:13px;

margin-top:5px;

}

.sidebar-title{

font-size:26px;

font-weight:bold;

color:white;

text-align:center;

}

.metric-card{

background:#1e293b;

padding:15px;

border-radius:15px;

margin-bottom:10px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SESSION
# -------------------------------------------------------

if "chatbot" not in st.session_state:
    st.session_state.chatbot = CustomerSupportChat()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    st.markdown(
        "<div class='sidebar-title'>🤖 AI Assistant</div>",
        unsafe_allow_html=True
    )

    st.success("Gemini Connected")

    st.divider()

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    st.metric(
        "Today's Date",
        datetime.now().strftime("%d %b %Y")
    )

    st.metric(
        "Status",
        "Online"
    )

    st.divider()

    if st.button(
        "🧹 New Chat",
        use_container_width=True
    ):

        st.session_state.messages=[]

        st.rerun()

    st.divider()

    st.markdown("### Features")

    st.write("✅ LangChain")

    st.write("✅ Google Gemini")

    st.write("✅ Intent Classification")

    st.write("✅ Knowledge Base")

    st.write("✅ AI Responses")

    st.write("✅ Conversation History")

    st.divider()

    st.info(
"""
Developer

**Nikhil Kanbarkar**

Machine Learning Enthusiast

AI | ML | Data Science
"""
    )

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.markdown(
"<div class='title'>🤖 AI Customer Support Assistant</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Powered by LangChain + Google Gemini</div>",
unsafe_allow_html=True
)

# -------------------------------------------------------
# SHOW OLD CHATS
# -------------------------------------------------------

for msg in st.session_state.messages:

    if msg["role"]=="user":

        st.markdown(
            f"""
<div class='user-box'>

👤 **You**

<br><br>

{msg['content']}

</div>
""",
unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
<div class='bot-box'>

🤖 **Assistant**

<br><br>

{msg['content']}

<div class='intent'>

Intent : {msg['intent']}

</div>

</div>
""",
unsafe_allow_html=True
        )

# -------------------------------------------------------
# INPUT
# -------------------------------------------------------

question = st.chat_input(
    "Ask anything..."
)

# -------------------------------------------------------
# USER INPUT
# -------------------------------------------------------

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.rerun()

# -------------------------------------------------------
# PROCESS LATEST USER MESSAGE
# -------------------------------------------------------

if (
    len(st.session_state.messages) > 0
    and st.session_state.messages[-1]["role"] == "user"
):

    latest_question = st.session_state.messages[-1]["content"]

    placeholder = st.empty()

    with placeholder.container():

        st.markdown(
            f"""
<div class='user-box'>

👤 <b>You</b>

<br><br>

{latest_question}

</div>
""",
            unsafe_allow_html=True
        )

        with st.spinner("🤖 Thinking..."):

            try:

                intent, response = (
                    st.session_state.chatbot.process_query(
                        latest_question
                    )
                )

            except Exception as e:

                intent = "System"

                response = f"❌ {str(e)}"

    # -----------------------------
    # STREAMING EFFECT
    # -----------------------------

    streamed = ""

    bot_placeholder = st.empty()

    words = response.split()

    for word in words:

        streamed += word + " "

        bot_placeholder.markdown(
            f"""
<div class='bot-box'>

🤖 <b>Assistant</b>

<br><br>

{streamed}▌

<div class='intent'>

Intent : {intent}

</div>

</div>
""",
            unsafe_allow_html=True
        )

        import time

        time.sleep(0.03)

    bot_placeholder.markdown(
        f"""
<div class='bot-box'>

🤖 <b>Assistant</b>

<br><br>

{response}

<div class='intent'>

Intent : {intent}

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "intent": intent
        }
    )

    st.session_state.chat_count += 1

    st.rerun()

# -------------------------------------------------------
# EMPTY SCREEN
# -------------------------------------------------------

if len(st.session_state.messages) == 0:

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
### 💡 Example Questions

• Where is my order?

• I want a refund.

• What payment methods do you accept?

• My laptop is not working.

• Do you provide express delivery?

• I forgot my password.
"""
        )

    with col2:

        st.success(
            """
### 🚀 Features

✅ AI Powered

✅ LangChain

✅ Google Gemini

✅ Intent Classification

✅ Knowledge Base

✅ Smart Responses

✅ Modern UI
"""
        )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:

    st.caption("🧠 LangChain")

with c2:

    st.caption("⚡ Google Gemini")

with c3:

    st.caption("🐍 Python")

st.markdown(
    """
<div style="text-align:center;
padding:20px;
color:gray;
font-size:14px;">

Made with ❤️ by <b>Nikhil Kanbarkar</b>

</div>
""",
    unsafe_allow_html=True
)

