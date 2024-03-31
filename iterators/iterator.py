"""
Custom iterator
"""

from dataclasses import dataclass


@dataclass
class CustomIterator:
    max_iterations: int

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == self.max_iterations:
            raise StopIteration("Has reached maximum iterations")
        else:
            print(f"Number of iteration: {self.n}")
            res = self.n
            self.n += 1
            return res


if __name__ == "__main__":
    custom_iterator = CustomIterator(max_iterations=3)
    iterator = iter(custom_iterator)

    for i in range(4):
        print(next(iterator))
