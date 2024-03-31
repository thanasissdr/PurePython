import time
from functools import wraps


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        value = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished {f.__name__} function in { end - start: .2f} seconds")
        return value

    return inner
