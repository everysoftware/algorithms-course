"""Задача на нахождение двух чисел в отсортированном массиве, сумма которых равна заданному числу."""


def sum_of_two_numbers_naive(arr: list[int], target: int) -> tuple[int, int]:
    n = len(arr)
    """Решение задачи перебором всех возможных комбинаций чисел в массиве. Сложность O(N^2)."""
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return i, j

    return -1, -1


def sum_of_two_numbers_tp(arr: list[int], target: int) -> tuple[int, int]:
    """Решение задачи с помощью двух указателей. Сложность O(N)."""
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return -1, -1
