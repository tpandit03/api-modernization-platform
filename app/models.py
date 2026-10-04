from pydantic import BaseModel,Field
class TransferRequest(BaseModel):
    from_account:str=Field(min_length=4)
    to_account:str=Field(min_length=4)
    amount:float=Field(gt=0)
    currency:str=Field(min_length=3,max_length=3)
class TransferResponse(BaseModel):
    transfer_id:str
    status:str
    correlation_id:str
