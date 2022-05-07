a = [0] * 10000
a[1] = 1
for i in range(1, 22 + 1):
    if i + 1 <= 22:
        a[i + 1] += a[i]
    if i * 3 <= 22:
        a[i * 3] += a[i]
for i in range(22, 70 + 1):
    if i + 1 <= 70:
        a[i + 1] += a[i]
    if i * 3 <= 70:
        a[i * 3] += a[i]
print(a[70])
