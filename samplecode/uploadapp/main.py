import random, string
from fastapi import FastAPI

app = FastAPI()

@app.get("/password/")
def get_password(length: int = 10, number: int = 10): 
    for _ in range(number):
        random_password = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        yield ''.join(random_password)   

if __name__ == "__main__":
    for i in get_password(10, 10):
        print(i)