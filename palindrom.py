def is_palindrom(s):
    return s[:len(s) // 2] == s[:(len(s) + len(s) % 2) // 2 - 1:-1]


print(['no', 'yes'][is_palindrom(input())])

# line = input()
# ans = 'yes'
# for i in range(len(line) // 2):
#     if line[i] != line[-1 - i]:
#         ans = 'no'
# print(ans)