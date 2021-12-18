def plus_one(x):
    return x + 1


def mul_two(x):
    return x * 2


for i in range(10, 28):
    s = i
    history = [[s]]

    for _ in range(2):
        heep = history[-1]
        temp = []
        for el in heep:
            temp.append(plus_one(el))
            temp.append(mul_two(el))
        history.append(temp)

    p1, p2 = max(history[1]), min(max(history[2][0], history[2][1]),
                               max(history[2][2], history[2][3]))

    if p1 < 29 and p2 >= 29:
        print(s)
