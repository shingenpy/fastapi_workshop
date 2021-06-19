from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
app = FastAPI()

def verify_user(username: str):
    if username == "taro":
        return username
    else:
        raise HTTPException(status_code=400, detail="User Invalid")

@app.get("/admin/", dependencies=[Depends(verify_user)])
def login():
    return {"msg": "Login Success!"}