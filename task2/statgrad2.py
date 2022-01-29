from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    if not (((x <= y) and (z or w)) <= ((x == w) or (y and not z))):
        print(x, y, z, w)
