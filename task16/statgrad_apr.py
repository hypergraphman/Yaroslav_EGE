def f(n):
    if n == 0:
        return 0
    t = n % 16
    if t != 0:
        return f(n - t) + t
    return f(n // 16)

print(f(255))


mx = 0
for i in range(1_600_000_000, 1_200_000_000, -1):
    t = f(i)
    if t > mx:
        mx = t
        print(mx)
