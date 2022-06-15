a = [0] * 3330
a[1] = 1
for i in range(1, 333):
    if i + 1 <= 333:
        a[i + 1] += a[i]
    if int(str(i) + '1') <= 333:
        a[int(str(i) + '1')] += a[i]
print(a[333])

