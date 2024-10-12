# This project is based on the original JavaScript version:
# https://github.com/Ai-Yolo/OpenAI-APIKey-Query
# Rewritten in Python using FastAPI and Streamlit by Claire

import streamlit as st
import requests

st.set_page_config(page_title="AI API Key Query", page_icon="🤖", layout="wide")

if "language" not in st.session_state:
    st.session_state.language = "en"

language = st.sidebar.radio("Select Language / 選擇語言", ["English", "繁體中文"], page_icon="🤖")

st.session_state.language = "zh-tw" if language == "繁體中文" else "en"

st.title("OpenAI API Key Query" if language == "English" else "查詢 OpenAI API 密鑰")

api_key = st.text_input("Enter API Key" if language == "English" else "輸入 API 密鑰", type="password")
start_date = st.date_input("Start Date" if language == "English" else "開始日期")
end_date = st.date_input("End Date" if language == "English" else "結束日期")

if st.button("Query" if language == "English" else "查詢"):
    api_url = f"http://backend:8000/openai/query/{st.session_state.language}"
    response = requests.post(api_url, json={"key": api_key, "start_date": str(start_date), "end_date": str(end_date)})

    if response.status_code == 200:
        data = response.json()
        st.table(data.items())
    else:
        st.error(f"Error: {response.json().get('detail')}")
