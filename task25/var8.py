def dels(n):
    res = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)


def f(n):
    d = dels(n)
    if len(d) > 3:
        # print(n, d[-1] - d[1], d[-1], d[1])
        return d[-2] - d[1]
    return 0


for i in range(850_000, 1000_000):
    t = f(i)
    if t > 0 and t % 11 == 0:
        print(i)