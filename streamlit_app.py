import streamlit as st
import requests

# Fetch question from backend
response = requests.get("http://localhost:8052/get_question?user_id=root")
question = response.json()["question"]

# Display question
st.header(question["question"])
user_answer = st.text_input("Your answer:")

if user_answer:
    # Send answer to backend
    requests.post("http://localhost:8052/submit_answer", json={"user_id": "root", "answer": user_answer})
    st.success("Correct! 🎉" if is_correct else "Try again ❌")
    
