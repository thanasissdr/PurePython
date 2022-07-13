"""
ProcessPoolExecutor will not work in jupyter notebook
and it will lead into errors
"""


import asyncio
import time

from functools import wraps
from concurrent.futures import ProcessPoolExecutor



def timing_async(f):
    @wraps(f)
    async def inner(*args, **kwargs):
        start = time.perf_counter()
        val = await f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Async function {f.__qualname__} finished in {end - start:.2f} seconds")
        return val

    return inner


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        val = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {f.__qualname__} finished in {end - start:.2f} seconds")
        return val

    return inner


def _simple_count(n=10000000):
    return [i for i in range(n)]


@timing_async
async def simple_count(n=100000000):
    executor = ProcessPoolExecutor(max_workers=1)
    loop = asyncio.get_event_loop()
    t = await loop.run_in_executor(executor, _simple_count, n)
    return t


@timing_async
async def sleep_short():

    await asyncio.sleep(0.05)
    return 10


@timing_async
async def sleep_long():
    await asyncio.sleep(1)
    return 20


async def main(n):
    tasks = [simple_count(n), sleep_short(), sleep_short()]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    N = 3000
    print(asyncio.run(main(N)))
