from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_invalid_amount_is_rejected():
    r=client.post("/v1/accounts/transfer",json={"from_account":"10001","to_account":"20002","amount":0,"currency":"USD"})
    assert r.status_code==422
