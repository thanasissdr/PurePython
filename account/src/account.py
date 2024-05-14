from dataclasses import dataclass
from typing import Self


class InsufficientFundsError(Exception):
    pass


class SelfTransferError(Exception):
    pass


@dataclass
class Account:
    id: int
    balance: float

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount

        else:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount} due to insufficient funds"
            )

    def transfer_to(self, account: Self, amount: float) -> None:
        if self != account:
            self._transfer_to(account, amount)
        else:
            raise SelfTransferError("Cannot transfer money from/to the same account id")

    def _transfer_to(self, account: Self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount

        else:
            raise InsufficientFundsError(
                f"Could not transfer amount {amount} to account_id: {account.id} from account_id: {self.id} due to insufficient funds."
            )

    def __eq__(self, account: Self) -> bool:
        return self.id == account.id


def deposit(account: Account, amount: float):
    account.deposit(amount)


def transfer(src: Account, dst: Account, amount: float) -> None:
    valid = False
    while not valid:
        try:
            src.transfer_to(dst, amount)
            valid = True
        except InsufficientFundsError:
            amount = float(input("Please insert a different amount to transfer: "))


def withdraw(account: Account, amount: float) -> None:
    valid = False
    while not valid:
        try:
            account.withdraw(amount)
            valid = True
        except InsufficientFundsError:
            amount = float(input("Please insert a different amount to withdraw: "))


def retrieve_account_from_data(id: int, data: list[dict]) -> Account | None:
    for account_data in data:
        file_account_id = account_data["id"]

        if str(id) == file_account_id:
            balance = float(account_data["balance"])
            return Account(id, balance)

    return None


def create_account(id: int) -> Account:
    balance = input(f"Please insert initial amount for account {id}: ")
    return Account(id, float(balance))


def account_factory(id: int, data: list[dict]) -> Account:
    account = retrieve_account_from_data(id, data)

    if account is None:
        account = create_account(id)

    return account
