import itertools

alf = (0, 1, 2, 3, 4)
s = set()
for num in itertools.product(alf, repeat=3):
    if num[0] >= num[1] >= num[2] and num[0] != 0:
        s.add(num)
print(len(s))