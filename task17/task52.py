start, end = 1000, 70000
c = 0
m = start
for i in range(start, end + 1):
    if 8**4 <= i < 8**5 and 5**5 <= i < 5**6 and i % 16**2 == 15 * 16 + 10:
        c += 1
        m = max(i, m)
print(c, m)