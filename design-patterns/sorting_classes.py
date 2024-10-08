from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import shuffle


@dataclass
class AbstractSortStrategy[T](ABC):
    @abstractmethod
    def run(self, data: list[T]) -> list[T]:
        pass


@dataclass
class Monotone[T: (int, float, str)](AbstractSortStrategy[T]):
    reverse: bool

    def run(self, data: list[T]):
        return sorted(data, reverse=self.reverse)


@dataclass
class Ascending[T: (int, float, str)](Monotone[T]):
    reverse: bool = False


@dataclass
class Descending[T: (int, float, str)](Monotone[T]):
    reverse: bool = True


class Identity[T: (int, float, str)](AbstractSortStrategy[T]):
    def run(self, data: list[T]):
        return data


class Shuffle[T: (int, float, str)](AbstractSortStrategy[T]):
    def run(self, data: list[T]):
        _data = data.copy()
        shuffle(_data)
        return _data


def sort_strategy_factory[T: (str, int, float)](
    sort_strategy: str,
) -> AbstractSortStrategy[T]:
    available_sort_strategies: dict[str, AbstractSortStrategy[T]] = {
        "ascending": Ascending(),
        "descending": Descending(),
        "identity": Identity(),
        "shuffle": Shuffle(),
    }

    selected_sort_strategy: AbstractSortStrategy[T] | None = (
        available_sort_strategies.get(sort_strategy)
    )
    if selected_sort_strategy is None:
        raise KeyError(
            f"Sort strategy '{sort_strategy}' is not supported. Available sort strategies are {list(available_sort_strategies)}"
        )

    return selected_sort_strategy


def main[T: (int, str, float)](data: list[T], sort_strategy: str) -> list[T]:
    sort_strategy_instance: AbstractSortStrategy[T] = sort_strategy_factory(
        sort_strategy
    )
    return sort_strategy_instance.run(data)


if __name__ == "__main__":
    DATA = [30, 0, 50, 10, 20, 40]
    SORT_STRATEGY = "descending"

    print(main(DATA, SORT_STRATEGY))
