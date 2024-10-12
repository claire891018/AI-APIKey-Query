from fastapi import APIRouter, HTTPException, Request
import requests

router = APIRouter()

@router.post("/query")
async def query_cohere_api(request: Request):
    data = await request.json()
    api_key = data.get("key")
    payload = data.get("payload", {})

    if not api_key:
        raise HTTPException(status_code=400, detail="API key is required")

    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api.cohere.ai/v1/generate"

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Cohere API Error: {str(e)}")
