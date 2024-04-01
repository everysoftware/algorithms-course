"""
https://contest.yandex.ru/contest/32588/problems/B/

Даны N точек на плоскости. Построить их выпуклую оболочку, т.е. наименьший выпуклый многоугольник, содержащий
все эти точки.

Формат ввода
В качестве входных данных заданы координаты точек на плоскости. Каждая пара координат начинается с новой строки,
значения в паре разделены пробелом.

Формат вывода
В качестве результата необходимо вывести строку "Convex Hull is:" и далее координаты точек, которые составляют
выпуклую оболочку. Каждая пара координат должна находиться на новой строке и использовать пробел в качестве
разделителя внутри строки.

Пример
Ввод
76 50
40 14
37 47
45 20
Вывод
Convex Hull is:
37 47
40 14
76 50
"""


def left_index(points: list[tuple[int, int]]) -> int:
    """
    Находит самую левую точку
    """

    left_most = 0

    for i in range(1, len(points)):
        if points[i][0] < points[left_most][0]:
            left_most = i
        elif points[i][0] == points[left_most][0]:
            if points[i][1] > points[left_most][1]:
                left_most = i

    return left_most


def orientation(
    p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]
) -> int:
    """
    Определяет ориентацию тройки точек (p, q, r)
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Построение выпуклой оболочки для заданных точек. Сложность O(N^2)"""
    n = len(points)

    left = left_index(points)
    point = left
    hull = []

    while True:
        hull.append(points[point])
        q = (point + 1) % n
        for r in range(n):
            if orientation(points[point], points[r], points[q]) == 2:
                q = r
        point = q
        if point == left:
            break

    hull.sort()

    return hull
