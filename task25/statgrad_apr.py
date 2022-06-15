def dels(n):
    res = {n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res


def m(k):
    t = 950_000_000
    divs = dels(t + k)
    even_divs = 0
    for el in divs:
        if el % 2 == 0:
            even_divs += 1
    return bool(even_divs % 2)


for k in range(10000, 1000000):
    if m(k):
        print(k)
# 44050*131232*218418*305608*392802 # считает 20 минут