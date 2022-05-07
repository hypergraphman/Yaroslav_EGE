def n_to_p(n, p):
    res = []
    while n > 0:
        res.append(n % p)
        n //= p
    return res


for n in range(2, 37):
    f = n**25 - 2 * n ** 13 + 10
    if sum(n_to_p(f, n)) == 75:
        print(n)
