import streamlit as st


def get_mistral_response(client, user_message):
    messages = [
        {
            "role": "system",
            "content": "You are an expert on Indian cities, places, and food. Keep answers concise and accurate.",
        },
        {"role": "user", "content": user_message},
    ]

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content


def run_indian_chatbot(client):
    st.subheader("Indian Expert Chatbot")

    if "indian_history" not in st.session_state:
        st.session_state.indian_history = []

    user_input = st.chat_input("Namaskar! Boliye...")

    if user_input:
        st.session_state.indian_history.append(
            {"role": "user", "content": user_input}
        )

        with st.spinner("🧠 Thinking..."):
            reply = get_mistral_response(client, user_input)

        st.session_state.indian_history.append(
            {"role": "assistant", "content": reply}
        )

    for chat in st.session_state.indian_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])