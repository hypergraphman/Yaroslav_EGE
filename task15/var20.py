for a in range(1000):
    f = True
    for x in range(100):
        for y in range(100):
            if not ((5 * x - 6 * y < a) or (x - y > 30)):
                f = False
                break
    if f:
        print(a)
        break