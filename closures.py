from dataclasses import dataclass


def closure():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


def generator():
    counter = 1

    while True:
        yield counter

        counter += 1


@dataclass
class Adder:
    counter: int = 0

    def run(self):
        self.counter += 1

        return self.counter


def run_closure() -> None:
    c = closure()

    for _ in range(3):
        print(c())


def run_generator() -> None:
    g = generator()

    for _ in range(3):
        print(next(g))


def run_adder() -> None:
    adder = Adder()

    for _ in range(3):
        print(adder.run())


if __name__ == "__main__":
    print("Running closure")
    run_closure()

    print("\nRunning generator")
    run_generator()

    print("\nRunning adder class")
    run_adder()
