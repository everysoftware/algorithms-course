"""
https://stepik.org/lesson/41234/step/5?unit=19818

Найти максимум в каждом окне размера m данного массива чисел A[1...n].

Вход. Массив чисел A[1...n] и число 1 ≤ m ≤ n.
Выход. Максимум подмассива A[i...i + m − 1] для всех 1 ≤ i ≤ n − m + 1.
"""

from collections import deque


def sliding_window_naive(m: int, a: list[int]) -> list[int]:
    """Наивное решение. Сложность O(NM)"""
    n = len(a)
    result = []

    for i in range(n - m + 1):
        result.append(max(a[i : i + m]))

    return result


def sliding_window_deque(m: int, a: list[int]) -> list[int]:
    """Решение с использованием очереди. Сложность O(N)"""
    n = len(a)
    d = deque()

    # Заполняем очередь для первого окна
    for i in range(m):
        # Удаляем элементы из окна, которые <= текущего
        while d and a[d[-1]] <= a[i]:
            d.pop()

        d.append(i)

    # Обрабатываем остальные окна
    result = []
    for i in range(m, n):
        # Добавляем максимум текущего окна
        result.append(a[d[0]])

        # Удаляем элементы, которые вышли из окна
        while d and d[0] <= i - m:
            d.popleft()

        # Удаляем элементы из окна, которые <= текущего
        while d and a[d[-1]] <= a[i]:
            d.pop()

        d.append(i)

    last_max = a[d.popleft()]
    result.append(last_max)

    return result
