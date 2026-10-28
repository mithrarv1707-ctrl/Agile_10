import pytest
from app import app, calculate_results

def test_calculation_logic():
    res = calculate_results([80, 90, 70])
    assert res["total"] == 240
    assert res["average"] == 80.0

def test_api_endpoint():
    client = app.test_client()
    response = client.post("/calculate", json={"marks": [100, 90]})
    assert response.status_code == 200
    assert response.json["total"] == 190
    assert response.json["average"] == 95.0

def test_health():
    client = app.test_client()
    assert client.get("/health").status_code == 200