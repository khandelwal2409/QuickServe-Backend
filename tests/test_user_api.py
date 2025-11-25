from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_menu():
    r = client.get("/api/user/menu")
    assert r.status_code == 200
    data = r.json()
    assert "menu" in data
    assert isinstance(data["menu"], list)
    # Basic structure checks
    assert all("category" in section and "items" in section for section in data["menu"])
