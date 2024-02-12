"""Бинарный поиск в отсортированном массиве."""

from typing import TypeVar

T = TypeVar("T")


def binary_search(
    a: list[T], target: T, start: int | None = None, end: int | None = None
) -> int:
    """Бинарный поиск в отсортированном массиве. Сложность O(log(N))."""
    start = start if start is not None else 0
    end = end if end is not None else len(a) - 1

    while start <= end:
        m = (start + end) // 2

        # Если x больше, игнорируем левую половину
        if a[m] < target:
            start = m + 1

        # Если x меньше, игнорируем правую половину
        elif a[m] > target:
            end = m - 1

        # Если x равен середине, возвращаем его индекс
        else:
            return m

    return -1
