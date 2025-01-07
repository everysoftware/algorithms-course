from typing import Any


# O(log(N))
def binary_search(a: list[int], target: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        # m = (start + end) // 2
        m = low + (high - low) // 2
        # Если target больше, игнорируем левую половину
        if a[m] < target:
            low = m + 1
        # Если target меньше, игнорируем правую половину
        elif a[m] > target:
            high = m - 1
        # Если target равен середине, возвращаем его индекс
        else:
            return m
    return -1


# O(log(N))
def local_binary_search(
    a: list[int],
    target: int,
    low: int = 0,
    high: int | None = None,
    *,
    key: Any = lambda x: x,
) -> int:
    high = high if high is not None else len(a) - 1
    while low <= high:
        # m = (start + end) // 2
        m = low + (high - low) // 2
        # Если target больше, игнорируем левую половину
        if a[m] < target:
            low = m + 1
        # Если target меньше, игнорируем правую половину
        elif a[m] > target:
            high = m - 1
        # Если target равен середине, возвращаем его индекс
        else:
            return m
    return -1
