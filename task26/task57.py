f = open('26-57.txt')
n, m = map(int, f.readline().split())
a = [int(x) for x in f.readlines()]
a.sort(reverse=True)
c = 0
i = 0
t = [a.pop(i)]
while sum(a) >= m:
    while sum(t) + a[i] >= m:
        i += 1
    if i == 0:
        t.append(a.pop(i))
    else:
        t.append(a.pop(i - 1))
        c += len(t) - 1
        a.append(sum(t) % m)
        i = 0
        t = [a.pop(i)]
    a.sort(reverse=True)

print(c, len(a))