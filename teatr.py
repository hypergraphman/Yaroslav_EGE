n, m = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]
s = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j]:
            s += costs[i][j]
print(s)
