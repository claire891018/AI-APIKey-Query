# This project is based on the original JavaScript version:
# https://github.com/Ai-Yolo/OpenAI-APIKey-Query
# Rewritten in Python using FastAPI and Streamlit by Claire

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_BASE_URL = "https://api.openai.com/v1"

@app.post("/api")
async def query_openai_api(request: Request):
    data = await request.json()
    api_key = data.get("key")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if not api_key:
        return {"error": "API Key is required"}

    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        usage_response = requests.get(
            f"{API_BASE_URL}/dashboard/billing/usage?start_date={start_date}&end_date={end_date}",
            headers=headers
        )
        usage_data = usage_response.json()

        return {"usage": usage_data}

    except Exception as e:
        return {"error": f"Failed to query API: {str(e)}"}
