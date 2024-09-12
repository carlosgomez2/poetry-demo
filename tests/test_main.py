import pytest
from fastapi.testclient import TestClient
from poetry_demo.main import app

# Crea un cliente de prueba para tu aplicación FastAPI
client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "Hello World"}


def test_read_item_with_query_param():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}


def test_read_item_without_query_param():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "Hello World"}


@pytest.fixture
def sample_data():
    return {"key": "value"}
