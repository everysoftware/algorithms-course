"""Нахождение делителей числа."""


def divisors_naive(n: int) -> list[int]:
    """Наивный поиск делителей. Сложность O(N)."""
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


def divisors(n: int) -> list[int]:
    """Эффективный поиск делителей. Сложность O(sqrt(N))."""
    lower, upper = [], []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)

    return lower + upper[::-1]
