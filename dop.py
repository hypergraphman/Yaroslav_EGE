from random import randint

n = 1000
a = []
for i in range(n):
    a.append(randint(1000, 100000))
print(a)


print(*filter(lambda s: s[:len(s) // 2] == s[:(len(s) + len(s) % 2) // 2 - 1:-1], [str(x) for x in a]))