import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"password" in r.data.lower()

def test_weak_password_shows_red(client):
    r = client.post("/check", data={"password": "abc"})
    assert r.status_code == 200
    assert b"d32f2f" in r.data