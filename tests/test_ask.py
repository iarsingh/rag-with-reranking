from fastapi.testclient import TestClient
from rerank.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'When is rollback allowed if the error rate doubles?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "a.md"
    miss = client.post("/ask", json={"question": 'lottery numbers'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
