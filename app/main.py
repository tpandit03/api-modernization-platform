from fastapi import FastAPI,Header
from .models import TransferRequest,TransferResponse
from .service import transfer
from .observability import record_request
app=FastAPI(title="API Modernization Platform",version="1.0.0")
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/v1/accounts/transfer",response_model=TransferResponse)
def create_transfer(request:TransferRequest,x_correlation_id:str|None=Header(default=None)):
    cid=x_correlation_id or "generated-correlation-id"
    record_request(cid,"account_transfer")
    return transfer(request,cid)
