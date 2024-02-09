"""
По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.
"""


def min_set_of_points(segments: list) -> list:
    s = sorted(segments, key=lambda x: x[1])
    sol = []
    i = 0
    while i <= len(s) - 1:
        seg = s[i]
        sol.append(seg[1])
        # скипаем пересекающиеся отрезки
        while i <= len(s) - 1 and s[i][0] <= seg[1]:
            i += 1
    return sol

