import string


def n_to_p(n, p):
    res = ''
    alf = string.digits + string.ascii_uppercase
    while n > 0:
        res = alf[n % p] + res
        n //= p
    return res


print(n_to_p(255, 16))