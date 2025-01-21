# O(n log n)
def min_set_of_points(segments: list[tuple[int, int]]) -> list[int]:
    n = len(segments)
    # Сортируем отрезки по правому концу.
    segments.sort(key=lambda x: x[1])
    cover = []
    i = 0
    while i < n:
        segment = segments[i]
        cover.append(segment[1])
        # Пропускаем пересекающиеся отрезки.
        while i < n and segments[i][0] <= segment[1]:
            i += 1
    return cover
