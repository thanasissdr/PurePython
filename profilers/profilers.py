import functools
import time
from line_profiler import LineProfiler
from decorator import decorator

from memory_profiler import profile as ram_profiler


@decorator
def cpu_profiler(f, *args, **kwargs):
    profiler = LineProfiler()
    profiled_func = profiler(f)
    try:
        profiled_func(*args, **kwargs)
    finally:
        profiler.print_stats()
    return f(*args, **kwargs)


def timing(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        value = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished {f.__name__} function in { end - start: .2f} seconds.")
        return value

    return inner
