from fastapi import FastAPI

app = FastAPI()

@app.get("/get1/")
def hello1():
    return {"hello": "world"}

@app.post("/post1/")
def hello2():
    return {"hello": "world"}

@app.put("/put1/")
def hello3():
    return {"hello": "world"}

@app.delete("/delete1/")
def hello4():
    return {"hello": "world"}
