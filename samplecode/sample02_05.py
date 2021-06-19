from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

@app.put("/body2/")
def body2_param(number: int = Body(...)):
    return number