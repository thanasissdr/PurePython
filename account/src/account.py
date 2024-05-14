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
