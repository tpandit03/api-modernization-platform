from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()["status"]=="ok"
def test_transfer():
    r=client.post("/v1/accounts/transfer",headers={"X-Correlation-ID":"test-123"},json={"from_account":"10001","to_account":"20002","amount":250,"currency":"USD"})
    assert r.status_code==200 and r.json()["status"]=="ACCEPTED" and r.json()["correlation_id"]=="test-123"
