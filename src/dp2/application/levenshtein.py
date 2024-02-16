"""
Минимальное кол-во вставок, удалений и замен символов, необходимое для преобразования
A в B называется расстоянием редактирования и расстоянием Левенштейна.
"""

"""
Выравнивание. Пример:
A = 'editing', B = 'distance'
A -> B:
E D I - T I N G -
- D I S T A N C E
Рассмотрим последний столбец оптимального выравнивания строк A и B.
Возможны 3 варианта:
1) вставка A[1...n], B[1...m] -> A[1...n] | -, B[1...m - 1] | B[m]
2) удаление A[1...n], B[1...m] -> A[1...n - 1] | A[n], B[1...m]
3) (не)соответствие A[1...n], B[1...m] -> A[1...n - 1] | A[n], B[1...m - 1] | B[m]
Для каждого из этих 3-х вариантов последнего столбца возможны 3 вариантов предпоследнего столбца.
"""

"""
Применим ДП.
Пусть D[i][j] - расстояние редактирования строк A[1...i] и B[1...j].
Тогда D[i][j] = min(
D[i, j - 1] + 1 (вставка),
D[i - 1, j] + 1 (удаление),
D[i - 1, j - 1] + isDiff(A[i], B[j]) не(соответствие)
)
"""


# O(N*M)
def edit_distance_td(a, b):
    n = len(a)
    m = len(b)
    d = [[float("inf")] * (m + 1) for _ in range(n + 1)]

    def edit_distance_help(i, j):
        if d[i][j] == float("inf"):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            else:
                ins = edit_distance_help(i, j - 1) + 1
                rem = edit_distance_help(i - 1, j) + 1
                sub = edit_distance_help(i - 1, j - 1) + (a[i - 1] != b[j - 1])
                d[i][j] = min(ins, rem, sub)
        return d[i][j]

    edit_distance_help(n, m)
    print(d)
    return d[n][m]


# можно заполнять таблицу строка за строкой или столбец за столбцом - O(N*M)
def edit_distance_bu(a, b):
    n = len(a)
    m = len(b)
    d = [[float("inf")] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = a[i - 1] != b[j - 1]
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c)
    return d[n][m]


"""
Чтобы восстановить решение, пойдём обратно от ячейки
d[n - 1][m - 1] к ячейке d[0][0].
Если d[i][j] = d[i - 1][j] + 1, то была произведено удаление
Если d[i][j] = d[i][j - 1] + 1, то было произведена вставка
Если d[i][j] = d[i - 1][j - 1] + isDiff(a[i], b[j]), то было (не)соответствие
"""


def edit_path_bu(a, b):
    n = len(a)
    m = len(b)
    d = [[float("inf")] * m for _ in range(n)]
    for i in range(n):
        d[i][0] = i
    for j in range(m):
        d[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = a[i] != b[j]
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c)
    return get_editing_path(a, b, d)
