from itertools import pairwise

a = list(map(int, open('17.txt').readlines()))
a_even = list(filter(lambda x: x % 2 == 0, a))
a_avg = sum(a_even) / len(a_even)
mx = 0
count = 0
for el1, el2 in pairwise(a):
    if (el1 % 3 == 0 and el2 < a_avg) or (el2 % 3 == 0 and el1 < a_avg):
        count += 1
        if mx < el1 + el2:
            mx = el1 + el2
print(count, mx)