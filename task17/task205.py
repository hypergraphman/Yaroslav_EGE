from itertools import pairwise
f = open('17-205.txt')
c = 0
mx = 0
for el1, el2 in pairwise(f.readlines()):
    el1, el2 = int(el1), int(el2)
    if (el1 - el2) % 2 == 0 and (el1 - el2) % 37 == 0:
        c += 1
        mx = max(mx, el1 + el2)
print(c, mx)