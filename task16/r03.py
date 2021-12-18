s = 0


def f(n):
    global s
    s += 2 * n
    if n > 1:
        s += n - 5
        f(n - 1)
        f(n - 2)


n = 5
while True:
    s = 0
    f(n)
    if s > 500000:
        print(n, s)
        break
    n += 1