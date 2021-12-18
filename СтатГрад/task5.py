def alg(n):
    n = str(n)
    s1 = 0
    for d in n:
        if int(d) % 2 == 0:
            s1 += int(d)
    s2 = 0
    for i in range(0, len(n), 2):
        s2 += int(n[i])
    return abs(s2 - s1)


for i in range(1, 100000):
    if alg(i) == 11:
        print(i)
        break