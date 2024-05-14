from .account import Account


def update_data(account: Account, data: list[dict]) -> list[dict]:
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
