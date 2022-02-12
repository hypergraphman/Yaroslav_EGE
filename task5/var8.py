def alg(n):
    t = n - n % 4
    t = bin(t)[2:]
    t = t + str(sum(map(int, t)) % 2)
    t = t + str(sum(map(int, t)) % 2)
    return int(t, 2)


for i in range(1, 48):
    if alg(i) < 47:
        print(i)