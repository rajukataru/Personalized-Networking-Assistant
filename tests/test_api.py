from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_generate():
    response = client.get("/generate", params={"event": "AI"})
    assert response.status_code == 200

def test_fact():
    response = client.get("/fact", params={"topic": "AI"})
    assert response.status_code == 200