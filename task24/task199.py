f = open('24-197.txt')
s = f.readline().strip()

max_len = 0
for j in range(3):
    cur_len = 0
    f = False
    for i in range(2 + j, len(s), 3):
        s1, s2, s3 = s[i - 2], s[i - 1], s[i]
        if s1 in 'XY' and s1 == s3:
            if not f:
                f = True
                cur_len = 1
            else:
                cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            f = False
    print(max_len)
