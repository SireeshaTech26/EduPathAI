
import streamlit as st
from agent import ask_agent

# Page configuration
st.set_page_config(
    page_title="EduPathAI",
    page_icon="🎓",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f7fc;
    color: #1e293b;
}

/* Header */
.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #2457a7 !important;
}

.subtitle {
    font-size: 17px;
    color: #64748b !important;
}

/* Chat messages */
.stChatMessage,
.stChatMessage p,
.stChatMessage li,
.stChatMessage h1,
.stChatMessage h2,
.stChatMessage h3,
.stChatMessage strong {
    color: #1e293b !important;
}

/* General text */
.stMarkdown,
.stMarkdown p,
.stMarkdown li {
    color: #1e293b !important;
}

/* Chat input container */
.stChatInput [data-baseweb="textarea"] {
    background-color: #000000 !important;
    border: 1px solid #475569 !important;
}

/* Chat input typed text */
.stChatInput textarea,
.stChatInput textarea:focus {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    background-color: #000000 !important;
    caret-color: #ffffff !important;
}

/* Chat input placeholder */
.stChatInput textarea::placeholder {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    opacity: 1 !important;
}

/* Subheaders */
h2, h3 {
    color: #2457a7 !important;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">🎓 EduPathAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Learn Smarter. Choose Better. Grow Further.</div>',
    unsafe_allow_html=True
)

st.divider()

st.subheader("Your Academic & Career Guide")

st.write(
    "Ask questions about your academic subjects, "
    "courses, careers, and internship opportunities."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask EduPathAI anything...")

if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("EduPathAI is thinking... Please wait."):
            try:
                answer = ask_agent(question)

                if not answer:
                    answer = "Sorry, I couldn't generate an answer. Please try again."

            except Exception as e:
                st.error(f"Error: {e}")
                answer = "Something went wrong. Please check the terminal."

        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
