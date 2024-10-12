import streamlit as st
import requests

st.title("Hugging Face API Query")

api_key = st.text_input("Enter Hugging Face API Key", type="password")
payload = st.text_area("Enter JSON payload")

if st.button("Query Hugging Face"):
    response = requests.post(
        "http://backend:8000/huggingface/query",
        json={"key": api_key, "payload": payload},
    )
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(f"Failed to query Hugging Face: {response.status_code}")
