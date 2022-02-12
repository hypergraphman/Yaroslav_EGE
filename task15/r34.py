for a in range(-100, 100):
    f = True
    for k in range(1, 100):
        for n in range(1, 100):
            if not ((5 * k + 6 * n > 57) or ((k <= a) and (n < a))):
                f = False
                break
        if not f:
            break
    if f:
        print(a)
        break