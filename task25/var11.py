def dels(n):
    res = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)


c = 6
n = 450000
while c:
    t = dels(n)
    if len(t) > 2 and len(dels(t[-2])) > 2:
        print(n, t[-2], dels(t[-2]))
        c -= 1
    n += 1
