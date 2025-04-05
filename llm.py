# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 14:42:01 2025

@author: HP
"""

import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCHQw_NQMUt-9vJMWF1pW6bbO4b5q4EfpI")  # Replace this!

# Use the correct model name from your available models
MODEL_NAME = "gemini-1.5-pro"

# Load the model
try:
    model = genai.GenerativeModel(MODEL_NAME)
    chat = model.start_chat(history=[])
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="Gemini 1.5 Chatbot", page_icon="💬")
st.title("💬 Gemini 1.5 Chatbot")

# Initialize history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", key="user_input")

# Send message
if user_input:
    st.session_state.chat_history.append(("user", user_input))

    try:
        response = chat.send_message(user_input)
        reply = response.text if response.text else "⚠️ No response text received."
        st.session_state.chat_history.append(("bot", reply))
    except Exception as e:
        st.session_state.chat_history.append(("bot", f"❌ Error: {e}"))

# Display chat
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Gemini:** {message}")

# Optional debug info
with st.expander("🔧 Debug"):
    try:
        models = genai.list_models()
        st.write("Available models:", [m.name for m in models])
    except Exception as e:
        st.write("Error listing models:", e)
