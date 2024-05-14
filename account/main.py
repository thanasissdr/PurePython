from src import FILEPATH
from src.account import account_factory
from src.data_updater import transfer
from src.file import read_csv

if __name__ == "__main__":
    data = read_csv(FILEPATH)

    account_1 = account_factory(id=9, data=data)
    account_2 = account_factory(id=6, data=data)

    transfer(account_1, account_2, 20)
