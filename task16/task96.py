from functools import cache


@cache
def f(n):
    if n < 10:
        return n
    return n % 10 + f(n // 10)


@cache
def g(n):
    if n < 10:
        return n
    return g(f(n))


s = 0
for i in range(10, 100):
    s += g(i)
print(s)