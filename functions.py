import functools
import time


def check_time(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"время работы функции: {end_time-start_time}")
        return wrapper()