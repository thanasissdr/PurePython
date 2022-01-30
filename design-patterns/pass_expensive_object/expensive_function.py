import time

from utils import timing


@timing
def run_expensive_function(seconds):
    print(f"Taking {seconds} seconds to run")
    time.sleep(seconds)
    output = 100
    print(f"The output of the expensive function is {output}")
    return output
