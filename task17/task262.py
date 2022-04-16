from itertools import pairwise

f = open('17-257.txt')
a = [int(x) for x in f.readlines()]

check = max(x for x in a if x % 2) + min(x for x in a if x % 2)
ans = []
for el1, el2 in pairwise(a):
    if (el1 + el2) % 2 == 0 and el1 + el2 > check:
        ans.append(el1 + el2)

print(len(ans), min(ans))