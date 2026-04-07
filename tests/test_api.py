from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_search():
    payload = {
        "resume_text": "Looking for Python developer with NLP experience",
        "skills": ["python", "nlp"]
    }

    response = client.post("/search", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "predicted_role" in data
    assert "top_candidates" in data
    assert isinstance(data["top_candidates"], list)