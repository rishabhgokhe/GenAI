import streamlit as st


def get_mistral_response(client, user_message):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content


def run_general_chatbot(client):
    st.subheader("General Chatbot")

    if "general_history" not in st.session_state:
        st.session_state.general_history = []

    user_input = st.chat_input("Type your message...")

    if user_input:
        st.session_state.general_history.append(
            {"role": "user", "content": user_input}
        )

        with st.spinner("🤖 Thinking..."):
            reply = get_mistral_response(client, user_input)

        st.session_state.general_history.append(
            {"role": "assistant", "content": reply}
        )

    for chat in st.session_state.general_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])