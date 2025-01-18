import bisect


# O((n + m)log(n + m))
def count_segments(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    m = len(points)
    events: list[tuple[int, int, int]] = []
    for left, right in segments:
        events.append((left, -1, 0))
        events.append((right, 1, 0))
    for i, point in enumerate(points):
        events.append((point, 0, i))
    events.sort()
    result = [0] * m
    # Сколько отрезков пересекаются с вертикальной прямой, проходящей через точку x
    count = 0
    for _, t, i in events:
        if t == 0:
            result[i] = count
        else:
            count -= t
    return result


# O(n log n + m log n) = O((n + m) log n)
def count_segments_bisect(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    x_all, y_all = [], []
    for segment in segments:
        x_all.append(segment[0])
        y_all.append(segment[1])
    x_all.sort()
    y_all.sort()
    result = []
    for point in points:
        # Сколько отрезков начинаются позже точки point
        x = bisect.bisect_right(x_all, point)
        # Сколько отрезков заканчиваются в точке point или позже
        y = bisect.bisect_left(y_all, point)
        result.append(x - y)
    return result
