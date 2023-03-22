def gcd_naive(x, y):
    res = 1
    for d in range(2, max(x, y)):
        if x % d == 0 and y % d == 0:
            res = d
    return res


'''
Пусть a >= b > 0 и r - остаток от деления a на b. Тогда
НОД(a, b) = НОД(r, b) <= НОД(a, b) = НОД(a - b, b).
Временная сложность: O(log(ab))
'''


def gcd_euclid(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(a, b % a)


def gcd_non_rec(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd(a, b):
    return gcd(b, a % b) if b else a


def test_gcd():
    print('Naive algorithm...')
    print(gcd_naive(14159572, 63967072))
    print('Euclid algorithm...')
    print(gcd(14159572, 63967072))
