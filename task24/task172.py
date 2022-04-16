f = open('24-171.txt')

max_len = 0
for line in f.readlines():
    s = line
    cur_len = 0
    prev = ''
    for el in s:
        if cur_len == 0 and el in 'XYZ' or cur_len > 0 and prev + el in ['XY', 'YZ', 'ZX']:
            cur_len += 1
            max_len = max(max_len, cur_len)
            prev = el
        else:
            if el in 'XYZ':
                cur_len = 1
                prev = el
            else:
                cur_len = 0
                prev = ''

print(max_len)