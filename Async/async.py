import asyncio
from multiprocessing.connection import Client
import requests
import time

from functools import wraps

from aiohttp import ClientSession


def timing_async(f):
    @wraps(f)
    async def inner(*args, **kwargs):
        start = time.perf_counter()
        val = await f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Async function {f.__qualname__} finished in {end - start:.2f} seconds.")
        return val

    return inner


@timing_async
async def quick_function():
    print("Entered quick function")
    return 1


async def _slow_function():
    print("Entered slow function")
    time.sleep(5)
    return 10


@timing_async
async def slow_function():
    slow_task = asyncio.create_task(_slow_function())
    return await slow_task


@timing_async
async def main():
    time.sleep(1)

    tasks = [quick_function(), slow_function(), quick_function()]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
