n, a, b, c, d = map(int, input().split())

arr = list(range(1, n + 1))
for i, j in [(a, b), (c, d)]:
    arr = arr[:i - 1] + arr[j - 1:i - 2:-1] + arr[j:]
print(*arr)