line = '1' * 93

while '2222' in line or '1111' in line:
    if '2222' in line:
        line = line.replace('2222', '11', 1)
    else:
        line = line.replace('1111', '22', 1)
print(line)
