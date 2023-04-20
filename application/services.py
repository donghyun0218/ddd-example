from domain.repositories import AccountRepository


class EmailService:
    def send_email(self, target_email: str, content: str):
        pass


class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def inquiry(self, user_id: int):
        account = self.repository.get_by_user_id(user_id)
        if not account:
            return None
        return account

    def withdraw(self, user_id: int, amount: int, email_service: EmailService):
        account = self.inquiry(user_id)
        if not account:
            raise
        account.withdraw(amount)
        self.repository.update(account)
        email_service.send_email('test@gmail.com', 'content')
        return account

    def deposit(self, user_id: int, amount: int, email_service: EmailService):
        account = self.inquiry(user_id)
        if not account:
            raise
        account.deposit(amount)
        self.repository.update(account)
        email_service.send_email('test@gmail.com', 'content')
        return account
