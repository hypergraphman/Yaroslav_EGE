def d(a, x):
    A = a % x == 0
    D730 = 730 % x == 0
    D110 = 110 % x == 0
    return not D730 or A or not D110


for a in range(35, 10000, 35):
    f = True
    for x in range(1, 1000):
        if not d(a, x):
            f = False
            break
    if f:
        print(a)
        break