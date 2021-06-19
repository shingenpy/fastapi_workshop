from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Human(BaseModel):
    name: str
    age: int

@app.put("/many/{number}")
def many_param(number: int, human: Human, q: int):
    return {"number": number, "human": human, "q": q}