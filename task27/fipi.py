f = open('27_B.txt')
n = int(f.readline())
a = [int(t) for t in f.readlines()]
print(n)
print(sum(a[0:1442152]), sum(a[0:1442152]) % 43)
print(sum(a[1442155:2732266]), sum(a[1442155:2732266]) % 43)
print(sum(a[2857143:3701301]), sum(a[2857143:3701301]) % 43)
print(sum(a[3701302:n]), sum(a[3701302:n]) % 43)