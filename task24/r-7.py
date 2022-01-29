line = open("k8-0.txt").readline()
mx = 1
cur_len = 1
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        cur_len += 1
        if cur_len > mx:
            mx = cur_len
            ans = i + 1 - mx
    else:
        cur_len = 1
print(mx)

cur_len = 1
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        cur_len += 1
        if cur_len == mx:
            print(line[i], mx)
    else:
        cur_len = 1