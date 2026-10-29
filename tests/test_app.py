from backend.app import app


def test_dashboard_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "UP"
    assert "timestamp" in data
def test_metrics_endpoint():
    client = app.test_client()
    response = client.get("/metrics")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "UP"
    assert data["application"] == "DevOps Monitoring Dashboard"
    assert data["uptime_seconds"] >= 0