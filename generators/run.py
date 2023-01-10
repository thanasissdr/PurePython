import time
from functools import wraps


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        val = f(*args, **kwargs)
        end = time.perf_counter()

        print(f"Function {f.__qualname__} finished in {end-start:.2f} seconds.")

        return val

    return inner


@timing
def get_squares_generator(n: int):
    """
    A generator should be preferred compared to
    a list comprehension if we want to apply
    `all` or `any` to a list
    """
    return any((x**2 for x in range(n)))


@timing
def get_squares_list_comprehension(n: int):
    return any([x**2 for x in range(n)])


def main(n: int):
    print(get_squares_generator(n))
    print(get_squares_list_comprehension(n))


if __name__ == "__main__":
    main(n=1000000)
