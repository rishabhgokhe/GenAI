import streamlit as st
from mistralai import Mistral

st.title("📌 Free Mistral API Chatbot")

MISTRAL_API_KEY = st.secrets["MISTRAL"]["api_key"]

if not MISTRAL_API_KEY:
    st.error("❗ Add your Mistral API key in .streamlit/secrets.toml")
    st.stop()

client = Mistral(api_key=MISTRAL_API_KEY)

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Enter your message:")


def get_mistral_response(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )

    return response.choices[0].message.content


if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Thinking..."):
        reply_text = get_mistral_response(user_input)

    st.session_state.history.append({"role": "assistant", "content": reply_text})


for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")

