import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_payment():
    response = client.post("/payments", json={
        "student_id": "60c72b2f9b1c8b551c6e6c2a",
        "school_id": "60c72b2f9b1c8b551c6e6c2b",
        "amount": 2800,
        "reference": "INV-12345"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "SUCCESS"

def test_get_school_revenue():
    response = client.get("/schools/60c72b2f9b1c8b551c6e6c2b/revenue")
    assert response.status_code == 200
    assert "total_collected" in response.json()
    assert "total_knit_fees" in response.json()
    assert "total_paid_to_school" in response.json()