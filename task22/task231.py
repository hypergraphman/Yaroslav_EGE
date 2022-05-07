for i in range(1000, 10000):
    s = i
    p = 29
    q = 11
    k1 = 0
    k2 = 0
    f = True
    while s != 2520:
        s = s + p
        k1 = k1 + 1
        if s > 2520:
            f = False
            print(i, 'error for # 1')
            break
    while f and s != q + k1 + k2:
        s = s - q
        k2 = k2 + 1
        if s < 0:
            f = False
            print(i, 'error for # 2')
            break
    k1 += s
    k2 += s
    if k1 == 314 and k2 == 470:
        print(i)
        break