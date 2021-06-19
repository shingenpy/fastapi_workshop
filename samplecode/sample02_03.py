from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/query2/")
def query2_param(number: int, q: Optional[int] = None):
    if q:
        return {"number": number, "q": q}
    else:
        return {"number": number}