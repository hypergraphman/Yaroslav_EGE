def n_to_p(n):
    res = []
    while n > 0:
        res.append(n % 4)
        n //= 4
    return res

print(n_to_p(2022))

for x in range(1, 100):
    f = 64**11 - 4**10 + 96 - x
    if sum(n_to_p(f)) == 71:
        print(x)
        break
