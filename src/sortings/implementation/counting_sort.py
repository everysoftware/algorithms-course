"""Сортировка подсчётом"""

from typing import Callable


def counting_sort(
    a: list[int], m: int, *, key: Callable[[int], int] | None = None
) -> list[int]:
    """Сортировка подсчётом с верхней границей M. Сложность O(N + M)."""
    n = len(a)
    keys = a if key is None else list(map(key, a))
    b = [0] * (m + 1)

    # Составляем b[i] - сколько раз встречается i
    for i in range(n):
        b[keys[i]] += 1

    # Делаем массив префиксных сумм (необходимо для стабильности сортировки),
    # b[i] - сколько раз встречаются числа не больше i.
    for i in range(1, m + 1):
        b[i] += b[i - 1]

    # Cортируем массив
    result = [0] * n
    for i in range(n - 1, -1, -1):
        result[b[keys[i]] - 1] = a[i]
        b[keys[i]] -= 1

    return result
