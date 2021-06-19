from fastapi import FastAPI 

app = FastAPI()

from fastapi import Path
from fastapi import Query

@app.get("/sample4/{id}/")
def validate_many(id: int = Path(..., ge=0),q: str = Query(..., regex="^sample.+")):
    return {"id": id, "q": q}