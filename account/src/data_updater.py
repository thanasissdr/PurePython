from typing import TYPE_CHECKING

from .file import read_csv, write_accounts_data

if TYPE_CHECKING:
    from .account import Account


def update_data(account: "Account", data: list[dict]) -> list[dict]:
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
        def inner(account, *args, **kwargs):
            data = read_csv(filepath)
            f(account, *args, **kwargs)
            data_updated = update_data(account, data)
            write_accounts_data(filepath, data_updated)

        return inner

    return wrapper
