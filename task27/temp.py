a = [12, 6, 19, 6, 41, 31, 10, 39, 7, 40, 3, 2, 40, 7, 1, 1]
for i in range(len(a)):
    for j in range(i, len(a)):
        if sum(a[i:j + 1]) % 43 == 0:
            print(i, j)