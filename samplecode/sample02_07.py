from fastapi import FastAPI
from typing import Optional
app = FastAPI()

from fastapi import Header
@app.get("/header/")
def header_param(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}