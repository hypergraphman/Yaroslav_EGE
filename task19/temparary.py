def plus_p(x, p):
    return x + p


def mul_p(x, p):
    return x * p


win = 46
move_1 = 1
move_2 = 3
for i in range(10, win):
    s = i
    h = [[s]]

    for _ in range(2):
        heep = h[-1]
        temp = []
        for el in heep:
            temp.append(plus_p(el, move_1))
            temp.append(mul_p(el, move_2))
        h.append(temp)

    p1, p2 = max(h[1]), min(max(h[2][0], h[2][1]), max(h[2][2], h[2][3]))

    if p1 < win <= p2:
        print(s)
