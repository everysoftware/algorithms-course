"""Сортировка подсчётом"""

from typing import Callable


def counting_sort(
    a: list[int], m: int, *, key: Callable[[int], int] | None = None
) -> list[int]:
    """Сортировка подсчётом с верхней границей M. Сложность O(N + M)."""
    n = len(a)
    keys = a if key is None else list(map(key, a))
    freq = [0] * (m + 1)
    """freq[i] - сколько раз встречается i"""

    for i in range(n):
        freq[keys[i]] += 1

    result = []
    for i, count in enumerate(freq):
        result.extend([i] * count)

    return result
