# Алгоритм Джарвиса, O(n^2)
def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    hull = []
    visited = set()
    # Считаем количество точек
    n = len(points)
    # Находим самую левую точку
    left = left_index(points)
    # Начинаем обход с самой левой точки
    point = left
    while True:
        # Добавляем точку в оболочку
        hull.append(points[point])
        visited.add(points[point])
        # Находим следующую точку
        q = (point + 1) % n
        for r in range(n):
            if orientation(points[point], points[r], points[q]) == 2:
                q = r
        # Учитываем коллинеарные точки - добавляем их в оболочку
        # Коллинеарные точки - это точки, лежащие на одной прямой с точками point и q
        for r in range(n):
            if r != point and r != q and orientation(points[point], points[q], points[r]) == 0:
                if on_segment(points[point], points[r], points[q]):
                    if points[r] not in visited:
                        hull.append(points[r])
                        visited.add(points[r])
        # Переходим к следующей точке
        point = q
        if point == left:
            break
    return hull


def left_index(points: list[tuple[int, int]]) -> int:
    left_most = 0
    for i in range(1, len(points)):
        if points[i][0] < points[left_most][0]:
            left_most = i
        elif points[i][0] == points[left_most][0]:
            if points[i][1] > points[left_most][1]:
                left_most = i
    return left_most


def orientation(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    # Коллинеарные точки
    if val == 0:
        return 0
    # Правый поворот
    elif val > 0:
        return 1
    # Левый поворот
    else:
        return 2


def on_segment(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> bool:
    # Проверяет, лежит ли точка q на отрезке pr
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
