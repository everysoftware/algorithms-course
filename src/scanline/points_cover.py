# O(n^2)
def points_cover_naive(points: list[float]) -> list[tuple[float, float]]:
    cover = []
    while points:
        # Находим минимальную точку.
        x_m = min(points)
        # Добавляем отрезок, начинающийся в этой точке.
        cover.append((x_m, x_m + 1))
        # Удаляем все точки, которые покрываются этим отрезком.
        points = [x for x in points if x > x_m + 1]
    return cover


# O(n log n)
def points_cover_scanline(points: list[float]) -> list[tuple[float, float]]:
    n = len(points)
    # Сортируем точки по возрастанию.
    points.sort()
    cover = []
    i = 0
    while i < n:
        # Добавляем отрезок, начинающийся в текущей точке
        segment = (points[i], points[i] + 1)
        cover.append(segment)
        i += 1
        # Пропускаем все точки, которые покрываются текущим отрезком
        while i < n and points[i] <= segment[1]:
            i += 1
    return cover
