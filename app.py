import streamlit as st
from mistralai import Mistral
from general_chatbot import run_general_chatbot
from indian_chatbot import run_indian_chatbot

st.set_page_config(page_title="Multi-Chatbot Hub", layout="wide")
st.title("🤖 All your Chatbots in one place")


try:
    MISTRAL_API_KEY = st.secrets["MISTRAL"]["api_key"]
except KeyError:
    st.error("⚠️ Add your Mistral API key in .streamlit/secrets.toml")
    st.stop()

client = Mistral(api_key=MISTRAL_API_KEY)

tab1, tab2 = st.tabs(["General Chatbot", "Indian Chatbot"])

with tab1:
    run_general_chatbot(client)

with tab2:
    run_indian_chatbot(client)