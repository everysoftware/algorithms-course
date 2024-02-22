"""
Функции для поиска нижней и верхней границы элемента в отсортированном массиве.
"""

from typing import Callable, Any


def lower_bound(
    a: list[int],
    x: int,
    left: int | None = None,
    right: int | None = None,
    *,
    key: Callable[[int], Any] | None = None,
) -> int:
    """
    Возвращает индекс первого элемента в диапазоне [left, right], который больше или равен x.
    Другими словами, возвращает индекс в отсортированном списке, где можно вставить элемент,
    чтобы сохранить отсортированный порядок списка. Сложность O(log(N)).
    """
    key = (lambda i: i) if key is None else key
    left = left if left is not None else 0
    right = right if right is not None else len(a) - 1

    while left <= right:
        m = (left + right) // 2

        if key(a[m]) >= x:
            right = m - 1
        else:
            left = m + 1

    return left


def upper_bound(
    a: list[int],
    x: int,
    left: int | None = None,
    right: int | None = None,
    *,
    key: Callable[[int], Any] | None = None,
) -> int:
    """
    Возвращает индекс первого элемента в диапазоне [left, right], который больше x.
    Другими словами, возвращает индекс, где элемент должен быть вставлен, если мы хотим вставить его
    после существующих элементов с таким же значением. Сложность O(log(N)).
    """
    key = (lambda i: i) if key is None else key
    left = left if left is not None else 0
    right = right if right is not None else len(a) - 1

    while left <= right:
        m = (left + right) // 2

        if key(a[m]) > x:
            right = m - 1
        else:
            left = m + 1

    return left
