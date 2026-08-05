import time
from datetime import datetime

import streamlit as st

from chat import CustomerSupportChat


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

.block-container{
padding-top:1.5rem;
padding-bottom:1rem;
padding-left:3rem;
padding-right:3rem;
max-width:1400px;
}

html,
body,
[class*="css"]{

font-family:"Segoe UI",sans-serif;
font-size:17px;

}

[data-testid="stAppViewContainer"]{

background:#0b1220;

}

[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #1f2937;

}

h1,h2,h3,h4,h5{

color:white;

}

.hero-title{

font-size:46px;

font-weight:700;

text-align:center;

color:white;

margin-bottom:0px;

}

.hero-sub{

text-align:center;

font-size:19px;

color:#9ca3af;

margin-bottom:30px;

}

.metric-card{

background:#182233;

padding:18px;

border-radius:14px;

border:1px solid #263244;

}

.section-title{

font-size:18px;

font-weight:600;

margin-bottom:10px;

color:white;

}

.chat-user{

background:#2563eb;

padding:18px;

border-radius:16px;

margin-bottom:18px;

color:white;

font-size:17px;

line-height:1.7;

}

.chat-ai{

background:#182233;

padding:18px;

border-radius:16px;

margin-bottom:22px;

border-left:5px solid #38bdf8;

color:white;

font-size:17px;

line-height:1.8;

}

.intent{

margin-top:15px;

font-size:13px;

color:#60a5fa;

font-weight:600;

}

.footer{

text-align:center;

padding-top:25px;

padding-bottom:10px;

color:#94a3b8;

font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION
# ==========================================================

if "chatbot" not in st.session_state:
    st.session_state.chatbot = CustomerSupportChat()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("## 🤖 AI Assistant")

    st.success("🟢 Gemini Connected")

    st.markdown("---")

    st.markdown("### 📊 Dashboard")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Chats",
            st.session_state.chat_count
        )

    with c2:
        st.metric(
            "Messages",
            len(st.session_state.messages)
        )

    st.metric(
        "Today",
        datetime.now().strftime("%d %b %Y")
    )

    st.metric(
        "Status",
        "Online"
    )

    st.markdown("---")

    if st.button(
        "🧹 New Chat",
        use_container_width=True,
        type="primary"
    ):

        st.session_state.messages = []
        st.session_state.chat_count = 0
        st.rerun()

    st.markdown("---")

    st.markdown("### 🚀 Technologies")

    st.markdown("""
- 🐍 Python
- 🦜 LangChain
- ✨ Google Gemini
- 📚 JSON Knowledge Base
- ⚡ Streamlit
""")

    st.markdown("---")

    st.markdown("### 💡 Supported Queries")

    st.caption("📦 Order Status")
    st.caption("💰 Returns & Refunds")
    st.caption("🛒 Product Inquiry")
    st.caption("🛠 Technical Support")
    st.caption("❓ General Questions")

    st.markdown("---")

    st.info(
"""
### 👨‍💻 Developer

**Nikhil Kanbarkar**

Machine Learning Enthusiast

Artificial Intelligence • Machine Learning • Data Science
"""
)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
"""
<div class="hero-title">
🤖 AI Customer Support Assistant
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="hero-sub">
Powered by <b>LangChain</b> • <b>Google Gemini</b> • <b>Streamlit</b>
</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# EMPTY SCREEN
# ==========================================================

if len(st.session_state.messages) == 0:

    left, right = st.columns([1.2,1])

    with left:

        st.markdown("### 💬 Try asking")

        st.info("""
📦 Where is my order?

💰 I want a refund

💳 Payment methods

🛠 My laptop is not working

🚚 Do you provide express delivery?

🔐 I forgot my password
""")

    with right:

        st.markdown("### ✨ Features")

        st.success("""
✅ AI Powered Responses

✅ Intent Classification

✅ Knowledge Base Retrieval

✅ LangChain Integration

✅ Google Gemini

✅ Conversation Memory

✅ Modern Interface
""")

    st.markdown("---")

# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message("user", avatar="👤"):

            st.markdown(message["content"])

    else:

        with st.chat_message("assistant", avatar="🤖"):

            st.markdown(message["content"])

            st.caption(f"Intent : {message['intent']}")

# ==========================================================
# CHAT INPUT
# ==========================================================

question = st.chat_input(
    "Ask your customer support question..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    st.rerun()

# ==========================================================
# PROCESS USER MESSAGE
# ==========================================================

if (
    len(st.session_state.messages) > 0
    and
    st.session_state.messages[-1]["role"] == "user"
):

    latest_question = st.session_state.messages[-1]["content"]

    with st.chat_message("assistant", avatar="🤖"):

        thinking = st.empty()

        thinking.info("🤖 Thinking...")

        try:

            intent, response = (
                st.session_state.chatbot.process_query(
                    latest_question
                )
            )

        except Exception as e:

            intent = "System"

            response = f"❌ {str(e)}"

        thinking.empty()

        stream_placeholder = st.empty()

        streamed_text = ""

        for word in response.split():

            streamed_text += word + " "

            stream_placeholder.markdown(
                streamed_text + "▌"
            )

            time.sleep(0.025)
        # ------------------------------------------
        # FINAL RESPONSE
        # ------------------------------------------

        stream_placeholder.markdown(response)

        st.caption(f"🎯 Intent : {intent}")

    # ------------------------------------------
    # SAVE RESPONSE
    # ------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "intent": intent
        }
    )

    st.session_state.chat_count += 1

    st.rerun()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Python",
        "3.x"
    )

with c2:
    st.metric(
        "Framework",
        "LangChain"
    )

with c3:
    st.metric(
        "Model",
        "Gemini"
    )

with c4:
    st.metric(
        "UI",
        "Streamlit"
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
"""
<div class="footer">

<b>🤖 AI Customer Support Assistant</b>

<br><br>

Powered by
<b>Python</b> •
<b>LangChain</b> •
<b>Google Gemini</b> •
<b>Streamlit</b>

<br><br>

Developed with ❤️ by
<b>Nikhil Kanbarkar</b>

</div>
""",
unsafe_allow_html=True
)