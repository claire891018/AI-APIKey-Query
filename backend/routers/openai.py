from fastapi import APIRouter, HTTPException, Request
import requests

router = APIRouter()

BALANCE_URL = "https://api.openai.com/v1/dashboard/billing/subscription"
USAGE_URL = "https://api.openai.com/v1/dashboard/billing/usage"

def get_balance_and_usage(api_key, start_date, end_date):
    headers = {"Authorization": f"Bearer {api_key}"}
    
    balance_response = requests.get(BALANCE_URL, headers=headers)
    balance_data = balance_response.json()

    usage_response = requests.get(f"{USAGE_URL}?start_date={start_date}&end_date={end_date}", headers=headers)
    usage_data = usage_response.json()

    return balance_data, usage_data

@router.post("/query/zh-tw")
async def query_openai_zh_tw(request: Request):
    """繁體中文查詢"""
    data = await request.json()
    api_key = data.get("key")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if not api_key:
        raise HTTPException(status_code=400, detail="需要提供 API Key")

    try:
        balance_data, usage_data = get_balance_and_usage(api_key, start_date, end_date)

        return {
            "帳戶名稱": balance_data.get("account_name", "未知"),
            "是否綁卡": "已綁卡" if balance_data.get("has_payment_method") else "未綁卡",
            "最近兩月已消費": f"{usage_data.get('total_usage', 0) / 100} USD",
            "每月消費上限": f"{balance_data.get('hard_limit_usd', 0)} USD",
            "帳戶餘額": f"{balance_data.get('soft_limit_usd', 0)} USD",
            "GPT-4 權限": "有" if "gpt-4" in balance_data.get("models", []) else "無",
            "有效期限": balance_data.get("expiry_date", "無")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查詢失敗：{str(e)}")

@router.post("/query/en")
async def query_openai_en(request: Request):
    """英文查詢"""
    data = await request.json()
    api_key = data.get("key")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    if not api_key:
        raise HTTPException(status_code=400, detail="API Key is required")

    try:
        balance_data, usage_data = get_balance_and_usage(api_key, start_date, end_date)

        return {
            "Account Name": balance_data.get("account_name", "Unknown"),
            "Has Payment Method": "Yes" if balance_data.get("has_payment_method") else "No",
            "Total Usage (Last 2 Months)": f"{usage_data.get('total_usage', 0) / 100} USD",
            "Monthly Limit": f"{balance_data.get('hard_limit_usd', 0)} USD",
            "Total Balance": f"{balance_data.get('soft_limit_usd', 0)} USD",
            "GPT-4 Access": "Yes" if "gpt-4" in balance_data.get("models", []) else "No",
            "Expiry Date": balance_data.get("expiry_date", "No Expiry")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to query OpenAI: {str(e)}")
