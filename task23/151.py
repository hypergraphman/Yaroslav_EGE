a = [0] * 10000
start = 9
end = 17
a[start] = 1
for i in range(start, end + 1):
    if i + 1 <= end:
        a[i + 1] += a[i]
    if i * 2 <= end:
        a[i * 2] += a[i]
    if i % 2 == 0 and i + 1 <= end:
        a[i + 1] += a[i]
    if i % 2 != 0 and i + 2 <= end:
        a[i + 2] += a[i]
print(a[end])
