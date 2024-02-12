"""Цифровая сортировка."""
from sortings.implementation import counting_sort


def get_d(x: int) -> int:
    """Возвращает количество разрядов числа."""
    d = 0
    while x > 0:
        d += 1
        x //= 10
    return d


def digit_sort(a: list[int]) -> list[int]:
    """Цифровая сортировка. Сложность O(DN), D - макс. число разрядов."""
    d = get_d(max(a))
    power = 1

    for i in range(d):
        a = counting_sort(a, 9, key=lambda x: (x // power) % 10)
        power *= 10

    return a
