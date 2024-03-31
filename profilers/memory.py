from functools import wraps
from typing import Callable

import psutil


def bytes_to_mb(data):
    return data / 10**6


def bytes_to_gb(data):
    return data / 10**9


def bytes_to_size_type_factory(size_type: str) -> Callable:
    available_size_transformers = {"GB": bytes_to_gb, "MB": bytes_to_mb}

    selected_transformer = available_size_transformers.get(size_type)
    if selected_transformer is None:
        raise KeyError(
            f"Size type {size_type} is not supported. Available sizes types are {list(available_size_transformers)}"
        )
    return selected_transformer


def convert_bytes_to_size_type(data: int, size_type: str):
    """
    Args:
        data: data in bytes
    """
    bytes_to_size_type_transformer = bytes_to_size_type_factory(size_type)
    data_transformed = bytes_to_size_type_transformer(data)
    return data_transformed


def ram_profiler(size_type: str):
    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            initial_memory = psutil.virtual_memory().used
            val = f(*args, **kwargs)
            final_memory = psutil.virtual_memory().used

            memory_diff = final_memory - initial_memory
            memory_diff_transformed = convert_bytes_to_size_type(memory_diff, size_type)

            print(
                f"Memory used by {f.__qualname__} is {memory_diff_transformed} {size_type}"
            )
            return val

        return inner

    return wrapper


@ram_profiler(size_type="MB")
def generate_large_strings(n):
    """
    Generates a list of `n` large strings.
    Each string is a repetition of a base pattern to ensure it occupies a substantial amount of memory.
    """
    base_pattern = "A" * 1024 * 1024  # 1MB string
    large_strings = [base_pattern * 10 for _ in range(n)]  # Each string is 10MB
    return large_strings


if __name__ == "__main__":
    generate_large_strings(10)
