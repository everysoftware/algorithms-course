"""
https://stepik.org/lesson/13249/step/6?thread=solutions&unit=3434

Даны отрезки на прямой и точки на прямой. Для каждой точки подсчитать, скольким отрезкам она принадлежит.

Формат входа. Первая строка содержит два числа 1 ≤ N ≤ 10^5 и 1 ≤ M ≤ 10^5 — количество отрезков и точек на прямой.
Следующие n строк содержат по два числа a_i, b_i (a_i ≤ b_i) — координаты концов отрезков.
Последняя строка содержит m чисел — координаты точек. Все координаты не превышают 10^8 по модулю.

Формат выхода. M чисел — для каждой точки количество отрезков, которым она принадлежит.
"""

from bisect import bisect_right, bisect_left


def points_and_segments_binary_search(
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
        x = bisect_right(x_all, point)  # сколько x >= point
        y = bisect_left(y_all, point)  # сколько y > point
        result.append(x - y)

    return result


def points_and_segments_event_sorting(
    segments: list[tuple[int, int]], points: list[int]
) -> list[int]:
    """Решает задачу о количестве отрезков, которым принадлежит каждая точка. Сложность O((N + M)log(N + M))."""
    m = len(points)
    events = []

    for left, right in segments:
        events.append((left, -1, None))
        events.append((right, 1, None))

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
