from fastapi import FastAPI
app = FastAPI()

@app.get("/path/{number}")
def path_param(number: int):
    # ここに処理を書く
    return {"number": number}