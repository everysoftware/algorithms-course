"""Быстрая сортировка."""

from .partition import partition2, partition3


def quick_sort2_helper(a: list[int], left: int, right: int) -> None:
    if left < right:
        m = partition2(a, left, right)
        quick_sort2_helper(a, left, m - 1)
        quick_sort2_helper(a, m + 1, right)


def quick_sort2(a: list[int]) -> None:
    """Быстрая сортировка. Сложность в среднем O(NlogN), в худшем O(N^2)."""
    quick_sort2_helper(a, 0, len(a) - 1)


def quick_sort3_helper(a: list[int], left: int, right: int) -> None:
    if left < right:
        k = (left + right) // 2
        a[left], a[k] = a[k], a[left]

        lower, upper = partition3(a, left, right)
        quick_sort3_helper(a, left, lower - 1)
        quick_sort3_helper(a, upper + 1, right)


def quick_sort3(a: list[int]) -> None:
    """Быстрая сортировка 3. Сложность O(NlogN)."""
    quick_sort3_helper(a, 0, len(a) - 1)
