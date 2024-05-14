from src.account import Account
from src.data_updater import update_data
from src.file import read_csv, write_accounts_data


def retrieve_account_from_data(id: int, data: list[dict]) -> Account | None:
    for account_data in data:
        file_account_id = account_data["id"]

        if str(id) == file_account_id:
            balance = float(account_data["balance"])
            return Account(id, balance)

    return None


def create_account(id: int) -> Account:
    balance = float(input(f"Please insert initial amount for account {id}: "))
    return Account(id, balance)


def account_factory(id: int, data: list[dict]) -> Account:
    account = retrieve_account_from_data(id, data)

    if account is None:
        account = create_account(id)

    return account


def main(id: int, filepath: str):
    data = read_csv(filepath)
    account = account_factory(id=id, data=data)
    account.deposit(50)
    updated_data = update_data(account, data)
    write_accounts_data(filepath, updated_data)


if __name__ == "__main__":
    FILEPATH = "./data.csv"

    main(id=23, filepath=FILEPATH)
