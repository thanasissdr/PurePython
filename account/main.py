from src import FILEPATH
from src.account import account_factory
from src.file import read_csv

if __name__ == "__main__":
    data = read_csv(FILEPATH)

    account = account_factory(id=7, data=data)
    account.withdraw(1)
