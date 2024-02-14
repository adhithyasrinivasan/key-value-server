import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_value_valid_key():
    response = client.get("/get_value/72cf48f7-d604-4423-b012-4e2329f5117b")
    assert response.status_code == 200
    assert response.json() == {"key": "72cf48f7-d604-4423-b012-4e2329f5117b", "value": "zsda pl focnygogk x cjuu cmwrolqrmu wgdwxr"}

def test_get_value_invalid_key():
    response = client.get("/get_value/3479d894-3271-4935-88cf-a06f3cbb80a6")
    assert response.status_code == 404
    assert response.json() == {"detail": "Key not found"}

def test_get_value_missing_key():
    response = client.get("/get_value/")
    assert response.status_code == 404