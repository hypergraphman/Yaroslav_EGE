def hod_a(s):
    if s % 2 == 0:
        return s // 2
    return s - 2


def hod_b(s):
    if s % 3 == 0:
        return s // 3
    return s - 3


for s in range(37, 4, -1):
    if hod_a((hod_a(s))) != 1 and hod_b((hod_a(s))) != 1 and hod_a((hod_b(s))) != 1 and hod_b((hod_b(s))) != 1:
        if hod_a(hod_a((hod_a(s)))) == 1 or hod_b(hod_a((hod_a(s)))) == 1:
            print('ход а от Пети и ход а от Вани ', s)
        if hod_a(hod_b((hod_a(s)))) == 1 or hod_b(hod_b((hod_a(s)))) == 1:
            print('ход а от Пети и ход b от Вани ', s)
        if hod_a(hod_a((hod_b(s)))) == 1 or hod_b(hod_a((hod_b(s)))) == 1:
            print('ход b от Пети и ход а от Вани ', s)
        if hod_a(hod_b((hod_b(s)))) == 1 or hod_b(hod_b((hod_b(s)))) == 1:
            print('ход b от Пети и ход b от Вани ', s)
