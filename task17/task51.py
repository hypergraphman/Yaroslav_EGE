start, end = 7**6, 7**7
c = 0
m = start
for i in range(start, end):
    if i % 3 == 2 and i % 8 != 3 and i % 12 != 5:
        c += 1
        m = max(i, m)
print(c, m)