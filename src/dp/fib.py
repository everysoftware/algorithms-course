"""
https://stepik.org/lesson/13228/step/6?unit=3414

Числами Фибоначчи называется последовательность чисел, в которой первое и второе числа равны 1, а каждое число
является суммой двух предыдущих.

Дано натуральное число N. Вычислите N-е число Фибоначчи.

Формат ввода
Вводится натуральное число N (1 <= N <= 100).

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод
10
Вывод
55
"""

from functools import lru_cache

"""
Это всего лишь рекуррентная формула для чисел Фибоначчи, это не динамическое программирование.

def fib_rec(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
"""


def _fib_cache(n: int, cache: dict[int, int]) -> int:
    if n < 2:
        return n

    if n not in cache:
        cache[n] = _fib_cache(n - 1, cache) + _fib_cache(n - 2, cache)

    return cache[n]


def fib_cache(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи с кэшированием. Сложность O(N)."""
    return _fib_cache(n, {})


@lru_cache(None)
def fib_lru_cache(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи с кэшированием с помощью lru_cache. Сложность O(N)."""
    if n < 2:
        return n
    else:
        return fib_lru_cache(n - 1) + fib_lru_cache(n - 2)


def fib_dp(n: int) -> int:
    """Вычисление числа Фибоначчи методом динамического программирования. Сложность O(N)."""
    a = [0] * (n + 1)
    a[1] = 1

    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[n]
