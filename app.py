# This project is based on the original JavaScript version:
# https://github.com/Ai-Yolo/OpenAI-APIKey-Query
# Rewritten in Python using FastAPI and Streamlit by Claire

import streamlit as st
import requests

st.title("OpenAI API Key Usage Query")

api_key = st.text_input("Enter your API Key", type="password")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Query Usage"):
    if not api_key:
        st.error("Please provide an API Key")
    else:
        response = requests.post(
            "http://localhost:8000/api",
            json={"key": api_key, "start_date": str(start_date), "end_date": str(end_date)}
        )
        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.success("Query successful!")
            st.json(data.get("usage"))