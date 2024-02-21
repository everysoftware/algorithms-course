"""Сортировка слиянием."""

from collections import deque

from sorting.implementation import merge


def merge_sort_helper(a: list[int], left: int, right: int) -> list[int]:
    if left >= right:
        return [a[left]] if len(a) > 0 else []

    m = (left + right) // 2
    # Производим слияние двух отсортированных кусков
    left_part = merge_sort_helper(a, left, m)
    right_part = merge_sort_helper(a, m + 1, right)

    return merge(left_part, right_part)


def merge_sort(a: list[int]) -> list[int]:
    """Сортировка слиянием. Сложность O(NlogN)."""
    return merge_sort_helper(a, 0, len(a) - 1)


def iterative_merge_sort(a: list[int]) -> list[int]:
    """Итеративная сортировка слиянием. Сложность O(NlogN)."""
    q = deque([a])

    while len(q) > 1:
        q.append(merge(q.popleft(), q.popleft()))

    result = q.popleft() if len(q) > 0 else []

    return result
