import streamlit as st
import requests

st.title("Cohere API Query")

api_key = st.text_input("Enter Cohere API Key", type="password")
payload = st.text_area("Enter JSON payload")

if st.button("Query Cohere"):
    response = requests.post(
        "http://backend:8000/cohere/query",
        json={"key": api_key, "payload": payload},
    )
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(f"Failed to query Cohere: {response.status_code}")