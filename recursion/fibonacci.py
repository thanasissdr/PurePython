def fib(n: int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(f"i: {i}, {fib(i)}")
