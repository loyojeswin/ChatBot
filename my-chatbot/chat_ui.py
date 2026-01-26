import streamlit as st
import requests
import json

st.title("🚀 My Smart Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# New message
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call your Flask API (run python ml_chatbot.py in another terminal first)
    try:
        response = requests.post("http://localhost:5000/chat", 
                                json={"message": prompt})
        bot_reply = response.json()["response"]
    except:
        bot_reply = "Start Flask server: python ml_chatbot.py"

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
