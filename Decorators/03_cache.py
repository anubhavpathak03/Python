import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper


def long_running_function(a, b):
    time.sleep(4)
    return (a + b)
