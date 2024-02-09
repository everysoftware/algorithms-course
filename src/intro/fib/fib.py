from functools import lru_cache


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


@lru_cache(None)
def fib_rec_cached(n):
    if n < 2:
        return n
    else:
        return fib_rec_cached(n - 1) + fib_rec_cached(n - 2)


def fib_table(n):
    if n < 2:
        return n
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]


def fib_two_last(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1 + fib2


def fib_approximate_formula(n):
    return 1.618 ** n / 5 ** 0.5


def fib_formula(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return int((phi ** n - psi ** n) / 5 ** 0.5)


def fib_last_digit(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, (fib1 + fib2) % 10
    return (fib1 + fib2) % 10


def fib_mod_two_last(n, m):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, (fib1 + fib2) % m
    return (fib1 + fib2) % m


def test_pisano():
    m = 13
    for n in range(100):
        print(fib_mod_two_last(n, m), end=' ')
    print()


def fib_mod_pisano(n, m):
    # используем периодичность
    if n < 2:
        return n
    a = [0] * (6 * m + 2)
    a[1] = 1
    a[2] = a[0] + a[1]
    i = 3
    while a[i - 1] != 1 or a[i - 2] != 0:
        a[i] = (a[i - 1] + a[i - 2]) % m
        i += 1
    return a[n % (i - 2)]


def test_fib():
    # Будет работать очень долго:
    # print(fib_rec(50))
    for i in range(10):
        print(fib_rec(i), end='\t')
    print()
    print(fib_rec(10))
    print(fib_rec_cached(50))
    print(fib_table(50))
    print(fib_two_last(50))
    print(fib_approximate_formula(50))
    print(fib_formula(50))
    print(fib_last_digit(50))
    print(fib_two_last(50) % 13, fib_mod_two_last(50, 13))
    test_pisano()
    print(fib_mod_pisano(50, 13))
    # expected 974
    print(fib_mod_pisano(60282445765134413, 2263))
