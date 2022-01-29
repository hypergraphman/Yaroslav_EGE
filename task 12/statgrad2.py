for i in range(16):
    line = '1' * (200 + i)
    while '1111' in line:
        line = line.replace('1111', '22', 1)
        line = line.replace('222', '1', 1)
        print(line)
    print(200 + i, line)