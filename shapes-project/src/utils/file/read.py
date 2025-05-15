import json
from typing import Any

from .characteristics import get_file_size, path_exists


class EmptyFileError(Exception):
    pass


def validate_path_exists(path: str) -> None:
    if not path_exists(path):
        raise FileNotFoundError(f"Path {path} does not exist")


def validate_file_is_not_empty(file: str) -> None:
    path_size = get_file_size(file)
    if path_size == 0:
        raise EmptyFileError(f"File {file} is empty")


def validate(f):
    VALIDATE_FNS = [validate_path_exists, validate_file_is_not_empty]

    def inner(file_path):
        for validate_fn in VALIDATE_FNS:
            validate_fn(file_path)
        return f(file_path)

    return inner


@validate
def load_json(file_path: str) -> Any:
    with open(file_path, "r") as f:
        return json.load(f)
