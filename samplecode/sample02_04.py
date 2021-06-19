from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Human(BaseModel):
    name: str
    age: int

@app.put("/body/")
def body_param(human: Human):
    return human