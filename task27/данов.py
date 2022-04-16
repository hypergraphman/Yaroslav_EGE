f = open('1.txt')
n = int(f.readline())
a = [int(s) for s in f]

k = 2
smax = -2**31
for i in range(n):
    s = t = 0
    for j in range(i, n):
        s += a[j]
        t += (a[j] > 0 and a[j] % 2 == 0)
        if t % k == 0 and s > smax:
            smax = s
print(smax)
print('----------')

k = 2
smax = -2**31
s = 0
t = 0
m = [2**31] * k
print(*a)
for x in a:
    s += x
    t += (x > 0 and x % 2 == 0)
    m[t % k] = min(s, m[t % k])
    if m[t % k] < 2**31:
        smax = max(smax, s - m[t % k])
    print(s, t, m[0], m[1], smax)

