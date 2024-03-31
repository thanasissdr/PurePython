"""
Generators
"""

import math
from typing import Generator


def is_even(n: int):
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 == 1


def is_prime(n: int) -> bool:
    if n in [0, 1]:
        return False

    if n == 2:
        return True

    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False

    return True


def generate_primes(n: int) -> Generator:
    """
    Get all the primes that are greater than n
    """

    while True:
        if is_even(n):
            n += 1
        else:
            if is_prime(n):
                yield n
            n += 2


if __name__ == "__main__":
    prime = generate_primes(100_000)

    for i in range(20):
        print(next(prime))
