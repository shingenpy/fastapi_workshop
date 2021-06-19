from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

@app.put("/signin/", response_model=UserOut)
def signup(user: UserIn):
    return user