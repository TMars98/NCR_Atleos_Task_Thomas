from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_existing_service_request():
    response = client.get("/service-requests/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["description"] == "Replace failed compressor on production line 3"
    assert body["customer_name"] == "Acme Manufacturing"

def test_missing_service_requests_resturns_404():
    response = client.get("/service-requests/999")
    assert response.status_code == 404

def test_non_integer_id_returns_422():
    response = client.get("/service-requests/abc")
    assert response.status_code == 422