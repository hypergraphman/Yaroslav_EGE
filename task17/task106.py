from math import sqrt, gcd, lcm


def n_divs(n):
    divs = {1, n}
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
    return len(divs)


start, end = 12356, 76435
c = 0
m = start
for i in range(start, end + 1):
    if n_divs(i) > 15:
        c += 1
        m = max(i, m)
print(c, m)