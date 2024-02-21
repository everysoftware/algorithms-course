"""Сортировка пузырьком"""


def bubble_sort(a: list[int]) -> None:
    """Сортировка пузырьком. Сложность O(N^2)."""
    n = len(a)

    for i in range(n - 1):
        for j in range(1, n):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
