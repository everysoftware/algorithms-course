from .partition import partition2, partition3


# O(N^2), O(NlogN) in average
def _quick_sort2(a: list[int], left: int, right: int) -> None:
    if left < right:
        m = partition2(a, left, right)
        _quick_sort2(a, left, m - 1)
        _quick_sort2(a, m + 1, right)


def quick_sort2(a: list[int]) -> None:
    _quick_sort2(a, 0, len(a) - 1)


# O(N^2), O(NlogN) in average
def _quick_sort3(a: list[int], left: int, right: int) -> None:
    if left < right:
        k = (left + right) // 2
        a[left], a[k] = a[k], a[left]

        lower, upper = partition3(a, left, right)
        _quick_sort3(a, left, lower - 1)
        _quick_sort3(a, upper + 1, right)


def quick_sort3(a: list[int]) -> None:
    _quick_sort3(a, 0, len(a) - 1)
