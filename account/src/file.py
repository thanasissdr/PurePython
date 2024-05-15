import csv
import os
import os.path as osp
from functools import wraps


class EmptyFileError(Exception):
    pass


def file_not_found_handler(f):
    @wraps(f)
    def inner(filepath: str, *args, **kwargs):
        if not osp.exists(filepath):
            raise FileNotFoundError(f"File {filepath} does not exist")
        return f(filepath, *args, **kwargs)

    return inner


@file_not_found_handler
def read_csv(filepath: str):
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return [line for line in reader]


@file_not_found_handler
def write_csv(filepath: str, data: list[dict], fieldnames: list[str]) -> None:
    with open(filepath, "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(data)


def write_accounts_data(
    filepath: str, data: list, fieldnames: list = ["id", "balance"]
):
    return write_csv(filepath, data, fieldnames)
