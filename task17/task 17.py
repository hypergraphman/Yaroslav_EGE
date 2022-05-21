with open('17.txt') as f:
    s = f.readlines()
    s = list(map(int, s))


t = list(filter(lambda x: x % 2, s))
sr = sum(t) / len(t)
c = 0
mx = 0
for i in range(2, len(s)):
    s1, s2, s3 = s[i - 2], s[i - 1], s[i]
    if {0, 1, 2} == {s1 % 3, s2 % 3, s3 % 3} and sorted([s1, s2, s3])[0] < sr and sorted([s1, s2, s3])[1] > sr:
        c += 1
        cur_sum = s1 + s2 + s3
        if cur_sum > mx:
            mx = cur_sum

print(c, mx)
