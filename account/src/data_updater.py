from src import FILEPATH

from .account import Account, InsufficientFundsError
from .file import read_csv, write_accounts_data


def update_account_data(account: Account, data: list[dict]) -> list[dict]:
    """
    :param data: holding accounts data
    :type data: list[str]
    """

    for account_data in data:
        if account_data["id"] == str(account.id):
            account_data["balance"] = account.balance
            return data

    data.append({"id": account.id, "balance": account.balance})
    return data


def update_file(filepath: str):
    def wrapper(f):
        def inner(*args, **kwargs):
            data = read_csv(filepath)
            f(*args, **kwargs)
            for arg in args:
                if isinstance(arg, Account):
                    data_updated = update_account_data(arg, data)
            write_accounts_data(filepath, data_updated)

        return inner

    return wrapper


@update_file(FILEPATH)
def deposit(account: Account, amount: float) -> None:
    account.deposit(amount)


@update_file(FILEPATH)
def transfer(src: Account, dst: Account, amount: float) -> None:
    valid = False
    while not valid:
        try:
            src.transfer_to(dst, amount)
            valid = True
        except InsufficientFundsError:
            amount = float(input("Please insert a different amount to transfer: "))


@update_file(FILEPATH)
def withdraw(account: Account, amount: float) -> None:
    valid = False
    while not valid:
        try:
            account.withdraw(amount)
            valid = True
        except InsufficientFundsError:
            amount = float(input("Please insert a different amount to withdraw: "))
