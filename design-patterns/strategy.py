from abc import ABC, abstractmethod
from typing import List


class ISort(ABC):
    @abstractmethod
    def run(self, data: List):
        pass


class SortReverse(ISort):
    def run(self, data: List):
        return sorted(data, reverse=True)


class Sort(ISort):
    def run(self, data: List):
        return sorted(data, reverse=False)


class SortingRunner:
    def __init__(self, sort_strategy: ISort):
        self.sort_strategy = sort_strategy

    def run(self, data: List) -> List:
        print("Running sorting algorithm")
        output = self.sort_strategy.run(data)
        print("Sorting algorithm finished")
        return output


if __name__ == "__main__":

    DATA = [3, 5, 2, 1, 4]
    STRATEGY = SortReverse()

    runner = SortingRunner(sort_strategy=STRATEGY)
    print(runner.run(DATA))
