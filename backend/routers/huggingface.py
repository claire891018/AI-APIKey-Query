from fastapi import APIRouter, HTTPException, Request
import requests

router = APIRouter()

@router.post("/query")
async def query_huggingface_api(request: Request):
    data = await request.json()
    api_key = data.get("key")
    payload = data.get("payload", {})

    if not api_key:
        raise HTTPException(status_code=400, detail="API key is required")

    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api-inference.huggingface.co/models/gpt2"

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Hugging Face API Error: {str(e)}")