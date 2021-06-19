from fastapi import FastAPI 

app = FastAPI()

@app.get("/200/", status_code=404)
def status_404():
    return {"msg": "status 404"}