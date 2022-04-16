def dels(n):
    res = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)


for i in range(2, 10000 + 1):
    if sum(dels(i)) == i:
        print(i, len(dels(i)))