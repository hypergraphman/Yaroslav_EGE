def dels(n):
    res = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res


def is_prime(n):
    return len(dels(n)) == 2


def only_prime_dels(n):
    t = dels(n)
    res = []
    for el in t:
        if is_prime(el):
            res.append(el)
    if res:
        return sum(res) // len(res)
    return 0


k = 0
i = 650000
while k != 4:
    f = only_prime_dels(i)
    if f % 37 == 23:
        print(i, f)
        k += 1
    i += 1
