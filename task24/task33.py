f = open('k7c-1.txt')
s = f.readline()
c = 0
for i in range(2, len(s)):
    if s[i - 2] in 'BCD' and \
       s[i - 1] in 'BDE' and s[i - 1] != s[i-2] and \
       s[i] in 'BCE' and s[i] != s[i - 1]:
        c += 1
print(c)