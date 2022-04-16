a = [0] * 10000
a[11] = 1
for i in range(11, 23 + 1):
    if i + 1 <= 23 and i != 17:
        a[i + 1] += a[i]
    if i + 2 <= 23 and i != 17:
        a[i + 2] += a[i]
for i in range(23, 29 + 1):
    if i + 1 <= 29:
        a[i + 1] += a[i]
    if i + 2 <= 29:
        a[i + 2] += a[i]
print(a[29])
