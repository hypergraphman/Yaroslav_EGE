f = open('24-180.txt')
s = f.readline()

mx_len = 0
for j in range(4):
    cur_len = 0
    for i in range(3 + j, len(s), 4):
        s1, s2, s3, s4 = s[i - 3:i + 1]
        h = int(s1 + s2)
        m = int(s3 + s4)
        if 0 <= h < 24 and 0 <= m < 60:
            cur_len += 1
            mx_len = max(mx_len, cur_len)
        else:
            cur_len = 0
print(mx_len)
