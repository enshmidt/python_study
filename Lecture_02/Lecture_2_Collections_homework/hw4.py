"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    is_called = dict()

    def wrapper(*arg):
        if id(func) not in is_called:
            res = func(*arg)
            is_called[id(func)] = res
            print("Result was counted")
            return res
        else:
            print("Get from cache")
            return is_called.get(id(func))
    return wrapper
