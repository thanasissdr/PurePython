from dataclasses import dataclass


@dataclass
class CustomIterator:
    max_iterations: int = 3
    n: int = 1

    def __next__(self):
        if self.n == self.max_iterations:
            raise StopIteration("Iteration reached its maximum number of iterations")

        else:
            x = self.n
            self.n += 1
        return x

    def __iter__(self):
        return self


def main(max_iterations: int = 3):
    custom_iter = CustomIterator(max_iterations=max_iterations)
    for i in range(max_iterations):
        print(next(custom_iter))


if __name__ == "__main__":
    main(max_iterations=3)
