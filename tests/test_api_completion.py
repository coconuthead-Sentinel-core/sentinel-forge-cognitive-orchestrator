from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_dashboard_metrics_returns_structured_payload():
    response = client.get("/api/dashboard/metrics")
    assert response.status_code == 200
    payload = response.json()
    assert "health_status" in payload
    assert "core" in payload
    assert "performance" in payload
    assert "cognition" in payload


def test_nexus_dashboard_metrics_route_is_distinct():
    response = client.get("/api/dashboard/nexus-metrics")
    assert response.status_code == 200
    payload = response.json()
    assert "active_nodes" in payload
    assert "clarity_score" in payload


def test_cognitive_status_reports_live_orchestrator_state():
    response = client.get("/api/cognitive/status")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "active"
    assert "default_lens" in payload
    assert "event_listener_running" in payload
    assert "orchestrator_metrics" in payload


def test_task_orchestration_start_and_stop_are_safe():
    start_response = client.post("/api/task/orchestrate/start")
    assert start_response.status_code == 200
    start_payload = start_response.json()
    assert start_payload["status"] == "initiated"
    assert start_payload["listener_running"] is True

    stop_response = client.post("/api/task/orchestrate/stop")
    assert stop_response.status_code == 200
    stop_payload = stop_response.json()
    assert stop_payload["status"] == "stopped"
    assert stop_payload["listener_running"] is False
