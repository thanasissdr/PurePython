from functools import wraps

import psutil


def cpu_profiler(f):
    @wraps(f)
    def inner(*args, **kwargs):
        # Capture the total CPU times (user + system) before function execution
        cpu_times_before = psutil.Process().cpu_times()

        val = f(*args, **kwargs)

        # Capture the total CPU times (user + system) after function execution
        cpu_times_after = psutil.Process().cpu_times()

        # Calculate the difference in CPU times
        user_time_used = cpu_times_after.user - cpu_times_before.user
        system_time_used = cpu_times_after.system - cpu_times_before.system

        print(
            f"{f.__name__} used {user_time_used:.2f} user and {system_time_used:.2f} system CPU seconds"
        )

        return val

    return inner


@cpu_profiler
def double_elements(n: int):
    for _ in range(n):
        [x**2 for x in range(10000)]


if __name__ == "__main__":
    double_elements(1000)
