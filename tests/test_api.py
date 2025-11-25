from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_get_item():
    payload = {"name": "Test Item", "description": "desc"}
    r = client.post("/api/items", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == payload["name"]
    item_id = data["id"]
    r2 = client.get(f"/api/items/{item_id}")
    assert r2.status_code == 200
    assert r2.json()["id"] == item_id
