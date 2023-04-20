from pydantic import BaseModel


class Owner(BaseModel):
    id: int
    name: str


class Account(BaseModel):
    id: int
    number: str
    owner: Owner
    balance: int = 0

    def withdraw(self, amount: int):
        if amount < 0:
            raise
        if self.balance < amount:
            raise
        self.balance -= amount

    def deposit(self, amount: int):
        if amount < 0:
            raise
        self.balance += amount
