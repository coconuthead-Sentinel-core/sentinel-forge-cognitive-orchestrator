from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# Test GET
response = client.get("/api/test")
print(f"GET /api/test: {response.status_code} - {response.text}")

# Test POST
response = client.post("/api/testpost", json={})
print(f"POST /api/testpost: {response.status_code} - {response.text}")

# Test the router POST
response = client.post("/api/testchat", json={"messages": []})
print(f"POST /api/testchat: {response.status_code} - {response.text}")