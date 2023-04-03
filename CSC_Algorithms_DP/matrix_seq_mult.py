"""
Нахождение оптимального порядка перемножения матриц
"""


# O(N^3)
def matrix_mult_td(m):
    n = len(m) - 1
    # d[i][j] мин. стоимость перемножения первых i
    d = [[float('inf')] * n for _ in range(n)]

    def matrix_mult_help(i, j):
        if d[i][j] == float('inf'):
            if i == j:
                d[i][j] = 0
            else:
                for k in range(i, j):
                    left = matrix_mult_help(i, k)
                    right = matrix_mult_help(k + 1, j)
                    d[i][j] = min(d[i][j], left + right + m[i - 1] * m[k] * m[j])
        return d[i][j]

    return matrix_mult_help(0, n - 1)


def matrix_mult_bu(m):
    n = len(m) - 1
    d = [[float('inf')] * n for _ in range(n)]
    # диагональ нулевая
    for i in range(n):
        d[i][i] = 0
    for s in range(n):
        for i in range(n - s):
            j = i + s
            # i, j: j - i = s
            for k in range(i, j):
                d[i][j] = min(d[i][j], d[i][k] + d[k + 1][j] + m[i - 1] * m[k] * m[j])
    return d[0][n - 1]
