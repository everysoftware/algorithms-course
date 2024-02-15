"""Проверка на простоту числа."""


def is_prime_naive(n: int) -> bool:
    """Наивная проверка на простоту. Перебор делителей от 2 до n-1. Сложность O(N)."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime(n: int) -> bool:
    """Проверка на простоту. Перебор делителей от 2 до sqrt(n). Сложность O(sqrt(N))."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
