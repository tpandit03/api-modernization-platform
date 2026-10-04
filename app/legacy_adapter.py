from uuid import uuid4
class LegacyTransferAdapter:
    def execute_transfer(self,from_account,to_account,amount,currency):
        return {"legacy_reference":f"LEG-{uuid4().hex[:10].upper()}","status":"ACCEPTED","amount":amount,"currency":currency}
