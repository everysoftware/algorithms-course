"""Быстрое возведение числа в степень"""


# https://leetcode.com/problems/powx-n/solutions/
def power(a: int, n: int) -> int:
    """Возведение числа в степень. Сложность O(N)."""
    result = 1

    for _ in range(n):
        result *= a

    return result


def fast_power(a: int, n: int) -> int:
    """Быстрое возведение числа в степень. Сложность O(log(N))."""
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * fast_power(a, n - 1)
    else:
        b = fast_power(a, n >> 1)
        return b * b
