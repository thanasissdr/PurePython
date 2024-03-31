type Float = float | int


def recursive_summation(arr: list[Float]) -> Float:
    if len(arr) == 1:
        return arr[0]
    else:
        first_element = arr.pop(0)
        return first_element + recursive_summation(arr)


if __name__ == "__main__":
    arr: list[Float] = [0, 1, 2, 10, 2.0]
    summa = recursive_summation(arr)
    print(summa)
