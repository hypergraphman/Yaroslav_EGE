a = 1
b = 0
for x in range(100000000, 1000000000):
    while x > 0:
        d = x % 9
        a *= d
        if d < 5:
            b += d
        x //= 9
if (a == 10) and (b ==9):
    print(x)