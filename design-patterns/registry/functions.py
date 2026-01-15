# pyright: reportOptionalCall=false

from random import shuffle as shuffler
from typing import Callable

config: dict[str, Callable] = {}


def register_sort_fn(name: str):
    def inner(fn: Callable):
        print(f"Registering function {fn.__qualname__} as '{name}'")
        config[name] = fn
        return fn

    return inner


@register_sort_fn("ascending")
def ascending(data: list):
    return sorted(data, reverse=False)


@register_sort_fn("descending")
def descending(data: list):
    return sorted(data, reverse=True)


@register_sort_fn("shuffle")
def shuffle(data: list):
    _data = data.copy()
    shuffler(_data)
    return _data


@register_sort_fn("identity")
def identity(data: list):
    return data


def main():
    data = [10, 50, 20, 40, 30]

    sort_strategy = "identity"
    sorting_fn = config.get(sort_strategy)
    print(sorting_fn(data))


if __name__ == "__main__":
    main()
