from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_search():
    response = client.post("/search", json={
        "resume_text": "Python developer with ML experience",
        "skills": ["Python", "ML"]
    })

    assert response.status_code == 200

    data = response.json()

    assert "predicted_role" in data
    assert "top_candidates" in data