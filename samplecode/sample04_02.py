from fastapi import FastAPI 

app = FastAPI()

@app.get("/sample2/")
def hinton(number: int):
    return {"number": number}