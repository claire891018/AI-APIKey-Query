# This project is based on the original JavaScript version:
# https://github.com/Ai-Yolo/OpenAI-APIKey-Query
# Rewritten in Python using FastAPI and Streamlit by Claire

from fastapi import FastAPI
from routers import openai, huggingface, cohere, anthropic

app = FastAPI()

app.include_router(openai.router, prefix="/openai", tags=["OpenAI"])
app.include_router(huggingface.router, prefix="/huggingface", tags=["Hugging Face"])
app.include_router(cohere.router, prefix="/cohere", tags=["Cohere"])
app.include_router(anthropic.router, prefix="/anthropic", tags=["Anthropic"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
