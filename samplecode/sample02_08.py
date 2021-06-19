from fastapi import FastAPI
from typing import Optional
app = FastAPI()

from fastapi import Cookie
@app.get("/cookie/")
def cookie_param(user_id: Optional[str] = Cookie(None)):
    return {"user_id": user_id}