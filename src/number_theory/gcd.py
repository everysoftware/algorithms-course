"""Наибольший общий делитель"""


def gcd_naive(a: int, b: int) -> int:
    """Наивный алгоритм нахождения НОД двух чисел. Сложность O(min(x, y))"""
    res = 1

    for d in range(2, min(a, b)):
        if a % d == 0 and b % d == 0:
            res = d

    return res


def gcd_euclid(a: int, b: int) -> int:
    """Алгоритм Евклида для нахождения НОД двух чисел. Сложность O(log(min(a, b)))"""
    while b != 0:
        a, b = b, a % b

    return a


def gcd_euclid_rec(a: int, b: int) -> int:
    """Рекурсивный алгоритм Евклида для нахождения НОД двух чисел. Сложность O(log(min(a, b)))"""
    if b == 0:
        return a

    return gcd_euclid_rec(b, a % b)
