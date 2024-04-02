import random
from typing import Callable


def _strategy_monotone(data: list, reverse: bool):
    return sorted(data, reverse=reverse)


def ascending(data: list):
    return _strategy_monotone(data, False)


def descending(data: list):
    return _strategy_monotone(data, True)


def identity(data: list):
    return data


def shuffle(data: list):
    _data = data.copy()
    random.shuffle(_data)
    return _data


def sort_strategy_factory(sort_strategy: str) -> Callable:
    available_sort_strategies = {
        "ascending": ascending,
        "descending": descending,
        "identity": identity,
        "shuffle": shuffle,
    }

    selected_sort_strategy_fn = available_sort_strategies.get(sort_strategy)
    if selected_sort_strategy_fn is None:
        raise KeyError(
            f"Sort strategy {sort_strategy} is not supported. Available sort strategies are {list(available_sort_strategies)}"
        )

    return selected_sort_strategy_fn


def main[T: str | float](data: list[T], sort_strategy: str) -> list[T]:
    sort_strategy_fn = sort_strategy_factory(sort_strategy)
    sorted_data = sort_strategy_fn(data)
    return sorted_data


if __name__ == "__main__":
    DATA = [20, 10, 40, 0, 50, 30]
    SORT_STRATEGY = "ascending"

    print(main(DATA, SORT_STRATEGY))
