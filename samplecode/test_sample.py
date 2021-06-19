from fastapi.testclient import TestClient
from sample import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello world"}