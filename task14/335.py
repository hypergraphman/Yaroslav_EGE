def n_to_p(n):
    res = []
    while n > 0:
        res.append(n % 4)
        n //= 4
    return res


n = 3 * 4**15 - 2 * 4**12 - 3 * 4**9 - 2022
t = set()
for x in range(16):
    t.add(sum(n_to_p(n - 4**x)))
print(len(t))
