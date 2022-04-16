f = open('var11_27_B.txt')
n = int(f.readline())
a = []
s = 0
for line in f.readlines():
    x, y = map(int, line.split())
    a.append(abs(x - y))
    s += max(x, y)

print(s)
print(s % 43)
a.sort()
for el in a:
    print(el, el % 43)
print(s)
print(s % 43)