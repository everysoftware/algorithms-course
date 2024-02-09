"""
Задача о выборе заявок. Сложность: O(NlogN).
"""


def act_sel(segments: list) -> list:
    s = sorted(segments, key=lambda x: x[1])
    sol = []
    i = 0
    while i <= len(s) - 1:
        seg = s[i]
        sol.append(seg)
        # Скипаем пересекающиеся отрезки.
        while i <= len(s) - 1 and s[i][0] < seg[1]:
            i += 1
    return sol
