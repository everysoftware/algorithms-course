from collections import deque

from .merge import merge


# O(NlogN)
def _merge_sort(a: list[int], left: int, right: int) -> list[int]:
    if left >= right:
        return [a[left]] if len(a) > 0 else []

    m = (left + right) // 2
    # Производим слияние двух отсортированных кусков
    left_part = _merge_sort(a, left, m)
    right_part = _merge_sort(a, m + 1, right)

    return merge(left_part, right_part)


def merge_sort(a: list[int]) -> list[int]:
    return _merge_sort(a, 0, len(a) - 1)


def iterative_merge_sort(a: list[int]) -> list[int]:
    q = deque([a])
    while len(q) > 1:
        q.append(merge(q.popleft(), q.popleft()))
    result = q.popleft() if len(q) > 0 else []
    return result
