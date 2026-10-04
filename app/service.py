from uuid import uuid4
from .legacy_adapter import LegacyTransferAdapter
adapter=LegacyTransferAdapter()
def transfer(request,correlation_id):
    result=adapter.execute_transfer(request.from_account,request.to_account,request.amount,request.currency)
    return {"transfer_id":f"TR-{uuid4().hex[:12].upper()}","status":result["status"],"correlation_id":correlation_id}
