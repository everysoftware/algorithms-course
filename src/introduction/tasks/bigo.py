"""Сортировка функций по скорости роста"""

from math import log, sqrt, factorial


def calculate(n: int) -> list[tuple[str, float]]:
    """Сортировка функций по скорости роста"""
    time = {
        # '2^(2^n)': 2 ** (2 ** n)
        "n!": factorial(n),
        "2^3n": 2 ** (3 * n),
        "4^n": 4**n,
        "2^n": 2**n,
        "n^sqrt(n)": n ** sqrt(n),
        "n^2": n**2,
        "sqrt(n)": sqrt(n),
        "log^2(n)": log(n, 2) ** 2,
        "7^log(n)": 7 ** log(n, 2),
        "n^log(n)": n ** log(n, 2),
        "3^log(n)": 3 ** log(n, 2),
        "log(log(n))": log(log(n, 2), 2),
        "log(n)^log(n)": log(n, 2) ** log(n, 2),
        "n/log(n)": n / log(n, 5),
        "sqrt(log(n))": sqrt(log(n, 4)),
        "log(n!)": log(factorial(n), 2),
        "log(n)": log(n, 3),
    }

    result = list(time.items())
    result.sort(key=lambda item: item[1])

    return result
