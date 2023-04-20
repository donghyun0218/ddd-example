from domain.models import Account
from domain.models import Owner
from domain.repositories import AccountRepository


class LocalMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.db = {
            1: Account(id=10, number='1111-3333-4444', owner=Owner(id=1, name='홍길동'), balance=50_000),
            2: Account(id=11, number='1111-5555-6666', owner=Owner(id=2, name='장영실'), balance=0),
        }

    def get_by_user_id(self, user_id: int) -> Account:
        return self.db.get(user_id)

    def create(self, account: Account) -> Account:
        self.db[account.owner.id] = account
        return account

    def update(self, account: Account) -> Account:
        stored_account = self.db.get(account.owner.id)
        if stored_account:
            self.db[account.owner.id] = account
        return account


class SqlAlchemyAccountRepository(AccountRepository):
    def __init__(self):
        pass

    def get_by_user_id(self, user_id: int) -> Account:
        return session.get_by_user_id(user_id)
