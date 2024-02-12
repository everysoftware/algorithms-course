"""Сортировка вставками."""


def insertion_sort(a: list[int]) -> None:
    """Сортировка вставками. Сложность O(N^2)."""
    n = len(a)

    for i in range(1, n):
        j = i
        # ставим элемент на его место
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
