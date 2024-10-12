from fastapi import APIRouter, HTTPException, Request
import requests

router = APIRouter()

@router.post("/query")
async def query_anthropic_api(request: Request):
    data = await request.json()
    api_key = data.get("key")
    payload = data.get("payload", {})

    if not api_key:
        raise HTTPException(status_code=400, detail="API key is required")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    url = "https://api.anthropic.com/v1/completions"

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Anthropic API Error: {str(e)}")