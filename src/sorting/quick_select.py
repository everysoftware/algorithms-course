"""Порядковая статистика в массиве"""

from .partition import partition2


def quick_select(a: list[int], k: int) -> int:
    """
    Поиск k-й порядковой статистики в массиве. Сложность в среднем O(N), в худшем O(N^2).
    """
    if len(a) == 1:
        return a[0]

    # Переводим k в индекс массива
    k -= 1

    left = 0
    right = len(a) - 1
    while True:
        pivot_index = partition2(a, left, right)

        if k == pivot_index:
            return a[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
