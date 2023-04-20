from fastapi import APIRouter

from application.services import AccountService
from infrastructure.repositories import LocalMemoryAccountRepository
from infrastructure.services import AwsEmailService
from presentation.models import DepositIn
from presentation.models import WithdrawalIn

router = APIRouter(
    prefix='/accounts',
    tags=['accounts'],
)


@router.get('/{user_id}')
async def inquiry_account(user_id: int):
    repository = LocalMemoryAccountRepository()
    service = AccountService(repository)
    account = service.inquiry(user_id)
    return account


@router.post('/{user_id}/withdraw')
async def withdraw(user_id: int, withdrawal_input: WithdrawalIn):
    repository = LocalMemoryAccountRepository()
    service = AccountService(repository)
    account = service.withdraw(user_id, **withdrawal_input.dict(), email_service=AwsEmailService())
    return account


@router.post('/{user_id}/deposit')
async def withdraw(user_id: int, deposit_input: DepositIn):
    repository = LocalMemoryAccountRepository()
    service = AccountService(repository)
    account = service.deposit(user_id, **deposit_input.dict(), email_service=AwsEmailService())
    return account
