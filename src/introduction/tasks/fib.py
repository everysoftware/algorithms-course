"""Вычисление чисел Фибоначчи различными способами."""


def fib_rec(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи. Сложность O(2^N)."""
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_two_last(n: int) -> int:
    """Вычисление числа Фибоначчи методом двух последних чисел. Сложность O(N)."""
    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2


def fib_formula(n: int) -> int:
    """
    Вычисление числа Фибоначчи по формуле Бине. Сложность O(1).

    Формула Бине для вычисления чисел Фибоначчи, зависит от точного вычисления и использования
    чисел с плавающей точкой. Однако, числа с плавающей точкой в компьютерах представлены с ограниченной точностью.

    Когда n становится очень большим (например, 100), phi**n и psi**n становятся очень большими и очень маленькими
    числами соответственно. Это может привести к значительным ошибкам округления из-за ограниченной точности чисел
    с плавающей точкой. В частности, psi**n становится настолько малым, что оно округляется до нуля, что приводит
    к потере точности в вычислениях.

    В результате, формула Бине может давать неточные результаты для больших значений n.
    Для больших n обычно используются другие методы вычисления чисел Фибоначчи, такие как динамическое
    программирование. Это обеспечивает более точные результаты и является более эффективным для больших n.
    """
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2

    return int((phi**n - psi**n) / 5**0.5)