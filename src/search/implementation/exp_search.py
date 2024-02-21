"""Экспоненциальный поиск"""

from .binary_search import binary_search


def exp_search(a: list[int], target: int) -> int:
    """Экспоненциальный поиск. Сложность O(log(i))"""
    n = len(a)
    end = 1

    while end < n and a[end] <= target:
        end *= 2

    end = min(end, n - 1)
    i = binary_search(a, target, end // 2, end)

    return i
