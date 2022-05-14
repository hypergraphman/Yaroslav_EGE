a = [0] * 10000
a[23] = 1
for i in range(23, 3 - 1, -1):
    if i - 2 >= 3:
        a[i - 2] += a[i]
    if i % 3 != 0 and i - i % 3 >= 3:
        a[i - i % 3] += a[i]
print(a[3])
