import streamlit as st
import requests

st.title("OpenAI API Query")

api_key = st.text_input("Enter OpenAI API Key", type="password")
payload = st.text_area("Enter JSON payload")

if st.button("Query OpenAI"):
    if not api_key:
        st.error("Please provide a valid API Key")
    else:
        response = requests.post(
            "http://backend:8000/openai/query",
            json={"key": api_key, "payload": payload},
        )
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Failed to query OpenAI: {response.status_code}")