"""
Задача о рюкзаке. Найти максимальный вес золота, который можно унести в рюкзаке.
Не разрешается брать часть предмета.
1. С повторениями - каждый предмет в неограниченном кол-ве
2. Без повторений - каждый предмет только 1
"""

"""
C ПОВТОРЕНИЯМИ
Рассмотрим оптимальное решение и предмет i в нём.
Если вытащить данный предмет из рюкзака, то мы получим
оптимальное заполнение рюкзака вместимости W - w_i (вырезать и вставить)
Подзадачи:
D[w] = макс. стоимость рюкзака вместимости w
Тогда:
D[w] = max_{i: w_i <= w}(D[w - w_i] + c_i)
"""


# O(N * W)
def knapsack_with_reps_bu(w, n, weight, cost):
    d = [0] * (w + 1)
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            if weight[j - 1] <= i:
                d[i] = max(d[i], d[i - weight[j - 1]] + cost[j - 1])
    return d[w]


"""
D[w - w_i] уже может не подойти, так как там уже может лежать i-й предмет.
Новые подзадачи:
D[w][i] - максимальная стоимость рюкзака вместимости w, если разрешено использовать первые i предметов
"""


# O(N * W)
def knapsack_without_reps_bu(w, n, weight, cost):
    d = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1]
            if weight[j - 1] <= i:
                d[i][j] = max(d[i][j], d[i - weight[j - 1]][j - 1] + cost[j - 1])
    return d[w][n]


def knapsack_td(w, n, weight, cost):
    h = {}

    def knapsack_td_help(i):
        if i not in h:
            v = 0
            for j in range(n):
                if weight[j] <= i:
                    v = max(v, knapsack_td_help(i - weight[j]) + cost[j])
            h[i] = v
        return h[i]

    return knapsack_td_help(w)


def golden_knapsack(w, n, weight):
    d = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1]
            if weight[j - 1] <= i:
                d[i][j] = max(d[i][j], d[i - weight[j - 1]][j - 1] + weight[j - 1])
    return d[w][n]
