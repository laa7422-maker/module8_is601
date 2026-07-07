# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# ---------- HOME PAGE ----------
def test_read_root():
    """The home page (index.html) should load successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


# ---------- ADD ----------
def test_add_endpoint():
    response = client.post("/add", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 15}


# ---------- SUBTRACT ----------
def test_subtract_endpoint():
    response = client.post("/subtract", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


# ---------- MULTIPLY ----------
def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 50}


# ---------- DIVIDE ----------
def test_divide_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 2}


# ---------- DIVIDE BY ZERO (returns 400 with "error" key) ----------
def test_divide_by_zero_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero!"}


# ---------- INVALID INPUT (validation error -> 400) ----------
def test_invalid_input():
    response = client.post("/add", json={"a": "not_a_number", "b": 5})
    assert response.status_code == 400
    assert "error" in response.json()
