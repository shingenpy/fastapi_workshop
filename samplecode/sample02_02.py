from fastapi import FastAPI
app = FastAPI()

@app.get("/query/")
def query_param(number: int):
    return {"number": number}