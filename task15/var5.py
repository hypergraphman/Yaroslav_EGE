for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        if not ((a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))):
            is_a = False
            break
    if is_a:
        print(a)
