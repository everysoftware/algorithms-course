"""
Покрывает набор точек минимальным числом единичных отрезков (O(N^2))
"""


def points_cover(points: list) -> list:
    s = points.copy()
    sol = []
    while s:
        x_m = min(s)
        sol.append([x_m, x_m + 1])
        s = [x for x in s if x > x_m + 1]
    return sol

'''
Покрывает набор точек минимальным числом единичных отрезков (O(NlogN))
'''
def points_cover_enhanced(points: list) -> list:
    s = sorted(points)
    sol = []
    i = 0
    while i <= len(s) - 1:
        seg = [s[i], s[i] + 1]
        sol.append(seg)
        i += 1
        while i <= len(s) - 1 and s[i] <= max(seg):
            i += 1
    return sol
