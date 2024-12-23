"""
https://stepik.org/lesson/13249/step/6

Даны отрезки на прямой и точки на прямой. Для каждой точки подсчитать, скольким отрезкам она принадлежит.

Формат входа. Первая строка содержит два числа 1 ≤ N ≤ 10^5 и 1 ≤ M ≤ 10^5 — количество отрезков и точек на прямой.
Следующие n строк содержат по два числа a_i, b_i (a_i ≤ b_i) — координаты концов отрезков.
Последняя строка содержит m чисел — координаты точек. Все координаты не превышают 10^8 по модулю.

Формат выхода. M чисел — для каждой точки количество отрезков, которым она принадлежит.

Пример.
Вход:
2 3
0 5
7 10
1 6 11

Выход:
1 0 0
"""

from bisect import bisect_right


def points_and_segments_bs(
    segments: list[tuple[int, int]], points: list[int]
) -> list[int]:
    """Решает задачу о количестве отрезков, которым принадлежит каждая точка. Сложность O((N + M)logN)."""
    x_all, y_all = [], []

    for segment in segments:
        x_all.append(segment[0])
        y_all.append(segment[1])

    x_all.sort()
    y_all.sort()

    result = []

    for point in points:
        # Сколько отрезков начинаются позже точки point или ровно в ней
        x = bisect_right(x_all, point)
        # Сколько отрезков заканчиваются позже точки point
        y = bisect_right(y_all, point - 1)

        result.append(x - y)

    return result


def points_and_segments_es(
    segments: list[tuple[int, int]], points: list[int]
) -> list[int]:
    """Решает задачу о количестве отрезков, которым принадлежит каждая точка. Сложность O((N + M)log(N + M))."""
    m = len(points)
    events: list[tuple[int, int, int]] = []

    for left, right in segments:
        events.append((left, -1, 0))
        events.append((right, 1, 0))

    for i, point in enumerate(points):
        events.append((point, 0, i))

    events.sort()

    result = [0] * m
    count = 0
    for x, t, i in events:
        if t == 0:
            result[i] = count
        else:
            count -= t

    return result
