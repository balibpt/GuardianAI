from fastapi import FastAPI, Body
from typing import Any
#create FastAPI app instance
app = FastAPI() 

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "GuardianAI is running"}

@app.get("/health")
def get_health() -> dict[str, Any]:
    return {"status": "ok", "models": ["text", "audio"]}

@app.post("/webhook")
async def webhook(payload: Any = Body(...)) -> dict[str, Any]:
    print("Raw Body: ", payload)
    return {"ok": True}
