from fastapi import FastAPI 

app = FastAPI()

@app.get("/sample1/")
def hintoff(number):
    return {"number": number}