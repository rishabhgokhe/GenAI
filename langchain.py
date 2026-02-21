from google import genai
import streamlit as st

API_KEY = st.secrets["GOOGLE"]["google_api_key"]
client = genai.Client(api_key=API_KEY)

def ask_math(question: str):
    prompt = f"""
You are a calculator that responds with math only.

Answer this math question: what is two plus two?
2+2=4

Answer this math question: {question}?
"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    return response.text

st.header("Langchain")

result = ask_math("what is square root of 25")
st.write(result)