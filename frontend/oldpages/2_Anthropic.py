import streamlit as st
import requests

st.title("Anthropic API Query (Claude)")

api_key = st.text_input("Enter Anthropic API Key", type="password")
payload = st.text_area("Enter JSON payload")

if st.button("Query Anthropic"):
    response = requests.post(
        "http://backend:8000/anthropic/query",
        json={"key": api_key, "payload": payload},
    )
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(f"Failed to query Anthropic: {response.status_code}")
