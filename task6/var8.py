for i in range(1, 100):
    s = i
    n = 2
    while s // n > 0:
        s -= 6
        n += 3
    if n == 17:
        print(i)