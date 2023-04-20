from domain.models import Account


class AccountRepository:
    def get_by_user_id(self, user_id: int) -> Account:
        pass

    def create(self, account: Account) -> Account:
        pass

    def update(self, account: Account) -> Account:
        pass
