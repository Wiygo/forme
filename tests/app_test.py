from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add():
    response = client.get("/add/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}

def test_subtract():
    response = client.get("/subtract/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

def test_multiply():
    response = client.get("/multiply/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}

def test_divide():
    response = client.get("/divide/?a=6&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

def test_divide_by_zero():
    response = client.get("/divide/?a=6&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}
