"""Бинарный поиск в отсортированном массиве."""


def binary_search(
    a: list[int], target: int, start: int | None = None, end: int | None = None
) -> int:
    """Бинарный поиск в отсортированном массиве. Сложность O(log(N))."""
    start = start if start is not None else 0
    end = end if end is not None else len(a) - 1

    while start <= end:
        m = (start + end) // 2

        # Если target больше, игнорируем левую половину
        if a[m] < target:
            start = m + 1

        # Если target меньше, игнорируем правую половину
        elif a[m] > target:
            end = m - 1

        # Если target равен середине, возвращаем его индекс
        else:
            return m

    return -1
