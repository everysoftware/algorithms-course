from math import log, sqrt, factorial


def calculate(n):
    return {
        # '2^(2^n)': 2 ** (2 ** n)
        # 'n!': factorial(n),
        # '2^3n': 2 ** (3 * n),
        # '4^n': 4 ** n,
        # '2^n': 2 ** n,
        # 'n^sqrt(n)': n ** sqrt(n),
        'n^2': n ** 2,
        'sqrt(n)': sqrt(n),
        'log^2(n)': log(n, 2) ** 2,
        '7^log(n)': 7 ** log(n, 2),
        'n^log(n)': n ** log(n, 2),
        '3^log(n)': 3 ** log(n, 2),
        'log(log(n))': log(log(n, 2), 2),
        'log(n)^log(n)': log(n, 2) ** log(n, 2),
        'n/log(n)': n / log(n, 5),
        'sqrt(log(n))': sqrt(log(n, 4)),
        'log(n!)': log(factorial(n), 2),
        'log(n)': log(n, 3)
    }


def test_bigo():
    f = calculate(100_000)
    print('Top functions:')
    for i, x in enumerate(sorted(f, key=lambda key: f[key])):
        print(str(i + 1) + ')', x, 'with result:', f[x])
