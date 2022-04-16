f = open('24-179.txt')
s = f.readline()
c = 0
letters = []
for i in range(4, len(s)):
    if s[i - 4] == 'C' and s[i - 3] == 'B' and (s[i - 2] not in 'ABF') and s[i - 1] == 'B' and s[i] == 'C':
        c += 1
        letters.append(s[i - 2])
for letter in 'CDE':
    print(letter, letters.count(letter))
print(c)
