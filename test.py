import pytest
from app import app, chat

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your question or prompt:" in response.data

def test_results(client):
    response = client.post("/results", data={"prompt": "Hello"})
    assert response.status_code == 200
    assert b"Prompt: Hello" in response.data
    assert b"Response:" in response.data

def test_chat():
    response = chat("Hello")
    assert len(response) > 0

def chat(prompt):
    url = "http://localhost:5000/chat"
    data = {"prompt": prompt}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.text}"
