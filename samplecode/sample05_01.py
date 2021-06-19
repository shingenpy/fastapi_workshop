from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

@app.put("/signin/")
def signup(user: UserIn):
    return user