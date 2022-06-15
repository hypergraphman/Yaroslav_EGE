with open('24.txt') as f:
    s = f.readline()

s = s.replace('D', 'C')
a = [len(x) for x in s.split('C')]
mx = 0
for i in range(len(a) - 3):
    if a[i] + a[i + 1] + a[i + 2] + a[i + 3]> mx:
        mx = a[i] + a[i + 1] + a[i + 2] + a[i + 3]
print(mx)