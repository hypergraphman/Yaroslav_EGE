win = 46
move_1 = 1
move_2 = 3

for s in range(1, win):
    if move_2 * s < win <= (s + move_1) * move_2:
        print(s)