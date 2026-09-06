from app.app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data == b"Application is healthy"


def test_readings():
    client = app.test_client()

    response = client.get("/readings")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 5
    assert data[0]["customer_id"] == "C10001"
