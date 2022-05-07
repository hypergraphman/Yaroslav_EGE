def dels(n):
    res = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return sorted(res)


num = 4679001
k = 5

while k > 0:
    dels_t = [el for el in dels(num) if len(dels(el)) == 2]
    t = ''.join(map(str, dels_t))
    if len(t) >= 5 and (t[0] == '2' and t[1] == '7' and t[-2] == '9' and t[-3] == '3' or \
            t[0] == '3' and t[1] == '4' and t[-1] == '7' and t[-3] == '2'):
        print(num, dels_t[-1])
        k -= 1
    num += 1

