from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import shuffle


@dataclass
class AbstractSortStrategy[T: str | float](ABC):
    @abstractmethod
    def run(self, data: list[T]) -> list[T]:
        pass


@dataclass
class Monotone(AbstractSortStrategy):
    reverse: bool

    def run(self, data):
        return sorted(data, reverse=self.reverse)


@dataclass
class Ascending(Monotone):
    reverse: bool = False


@dataclass
class Descending(Monotone):
    reverse: bool = True


class Identity(AbstractSortStrategy):
    def run(self, data):
        return data


class Shuffle(AbstractSortStrategy):
    def run(self, data):
        _data = data.copy()
        shuffle(_data)
        return _data


def sort_strategy_factory(sort_strategy: str) -> AbstractSortStrategy:
    available_sort_strategies = {
        "ascending": Ascending(),
        "descending": Descending(),
        "identity": Identity(),
        "shuffle": Shuffle(),
    }

    selected_sort_strategy = available_sort_strategies.get(sort_strategy)
    if selected_sort_strategy is None:
        raise KeyError(
            f"Sort strategy '{sort_strategy}' is not supported. Available sort strategies are {list(available_sort_strategies)}"
        )

    return selected_sort_strategy


def main[T: str | float](data: list[T], sort_strategy: str) -> list[T]:
    sort_strategy_instance = sort_strategy_factory(sort_strategy)
    return sort_strategy_instance.run(data)


if __name__ == "__main__":
    DATA = [30, 0, 50, 10, 20, 40]
    SORT_STRATEGY = "descending"

    print(main(DATA, SORT_STRATEGY))
