from dataclasses import dataclass
from typing import Self


class InsufficientFundsError(Exception):
    pass


class SelfTransferError(Exception):
    pass


@dataclass
class Account:
    id: int
    balance: float = 0

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError(
                f"Could not withdraw amount {amount} due to insufficient funds"
            )

    def transfer_to(self, account: Self, amount: float) -> None:
        if self != account:
            self._transfer_to(account, amount)
        else:
            raise SelfTransferError("Cannot apply self transfer")

    def _transfer_to(self, account: Self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount

        else:
            raise InsufficientFundsError(
                f"Could not transfer amount {amount} to account with account_id: {account.id} due to insufficient funds"
            )

    def __eq__(self, account: Self) -> bool:
        return self.id == account.id


if __name__ == "__main__":
    account_1 = Account(id=1, balance=10_000)
    account_2 = Account(id=2, balance=500)

    account_1.deposit(1_000)
    account_1.withdraw(1500)
    account_1.transfer_to(account_2, 2_000)
    account_2.withdraw(50)

    print(account_1)
    print(account_2)
