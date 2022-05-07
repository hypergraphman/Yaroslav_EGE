line = '132abc33422234as1111df234234'
s = line.strip('1234567890')
cur_len = 0
max_len = 0
f = False
prev_el = ''
for el in s:
    if el.isdigit():
        if f and prev_el == el:
            cur_len += 1
        else:
            cur_len = 1
            prev_el = el
            f = True
        max_len = max(max_len, cur_len)
    else:
        f = False
print(max_len)
