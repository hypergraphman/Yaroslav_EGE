import functools


@functools.lru_cache(maxsize=1000)
def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(50))