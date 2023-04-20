from pydantic import BaseModel


class WithdrawalIn(BaseModel):
    amount: int


class DepositIn(BaseModel):
    amount: int
