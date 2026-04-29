# O(n)
def is_reflected(points: list[list[int]]) -> bool:
    min_x, max_x = float("inf"), float("-inf")
    points_set = set()
    # Находим минимальное и максимальное значение x.
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        points_set.add((x, y))
    s = min_x + max_x
    # Проверяем, что для каждой точки (x, y) существует точка (s - x, y).
    return all((s - x, y) in points_set for x, y in points)
