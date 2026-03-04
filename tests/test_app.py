from src.app import app


def client():
    return app.test_client()


def test_healthz_status_code():
    c = client()
    resp = c.get("/api/v1/healthz")
    assert resp.status_code == 200


def test_healthz_payload():
    c = client()
    resp = c.get("/api/v1/healthz")
    data = resp.get_json()
    assert data["message"] == "Hello World - healthz"
    assert data["status"] == "up"
    assert "hostname" in data
    assert "time" in data


def test_details_endpoint():
    c = client()
    resp = c.get("/api/v1/details")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "Hello World - details"
    assert data["action"].startswith("Success from details endpoint")

