c = 0
for i in range(10_000_000, 100_000_000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        d = x % 10
        if d % 3 == 0:
            b += d
        x //= 10
    if a == 8 and b == 66:
        c += 1
        print(c, i)
