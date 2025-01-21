from collections import deque
from typing import Callable

from src.d_sorting.merge import merge
from src.d_sorting.partition import partition2, partition3


# O(n^2), O(n log n) в среднем, TLE на больших входах
def quick_sort(a: list[int]) -> None:
    _quick_sort(a, 0, len(a) - 1)


# O(n^2), O(n log n) в среднем, TLE на больших входах
# QuickSort3 is more efficient than QuickSort on arrays with many duplicate elements
def quick_sort3(a: list[int]) -> None:
    _quick_sort3(a, 0, len(a) - 1)


# O(n log n)
def merge_sort(a: list[int]) -> list[int]:
    return _merge_sort(a, 0, len(a) - 1)


# O(n log n)
def iterative_merge_sort(a: list[int]) -> list[int]:
    q = deque([[x] for x in a])
    while len(q) > 1:
        left_part = q.popleft()
        right_part = q.popleft()
        merged = merge(left_part, right_part)
        q.append(merged)
    result = q.popleft() if len(q) > 0 else []
    return result


# O(n)
def counting_sort(
    a: list[int],
    key: Callable[[int], int] | None = None,
) -> list[int]:
    if not a:
        return a
    keys = a if key is None else list(map(key, a))
    min_val, max_val = min(keys), max(keys)
    # Массив частот
    freq_size = max_val - min_val + 1
    freq = [0] * freq_size
    for k in keys:
        freq[k - min_val] += 1
    # Префиксные суммы
    for i in range(1, freq_size):
        freq[i] += freq[i - 1]
    # Сортировка
    result = [0] * len(a)
    for i in range(len(a) - 1, -1, -1):
        k = keys[i]
        freq[k - min_val] -= 1
        result[freq[k - min_val]] = a[i]
    return result


# O(n)
def radix_sort(nums: list[int]) -> list[int]:
    if not nums:
        return nums
    min_val = min(nums)
    nums = [num - min_val for num in nums]
    max_val = max(nums)
    factor = 1
    while max_val // factor > 0:
        nums = counting_sort(nums, key=lambda x: (x // factor) % 10)
        factor *= 10
    return [num + min_val for num in nums]


def _quick_sort(a: list[int], left: int, right: int) -> None:
    if left >= right:
        return
    m = partition2(a, left, right)
    _quick_sort(a, left, m - 1)
    _quick_sort(a, m + 1, right)


def _quick_sort3(a: list[int], left: int, right: int) -> None:
    if left >= right:
        return
    k = (left + right) // 2
    a[left], a[k] = a[k], a[left]
    lower, upper = partition3(a, left, right)
    _quick_sort3(a, left, lower - 1)
    _quick_sort3(a, upper + 1, right)


def _merge_sort(a: list[int], left: int, right: int) -> list[int]:
    if left >= right:
        return [a[left]] if len(a) > 0 else []
    m = (left + right) // 2
    left_part = _merge_sort(a, left, m)
    right_part = _merge_sort(a, m + 1, right)
    return merge(left_part, right_part)
