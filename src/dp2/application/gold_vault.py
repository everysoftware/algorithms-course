"""
https://stepik.org/lesson/13259/step/5?unit=3444

Вы собираетесь ограбить золотохранилище. Первая строка входа содержит вместимость рюкзака W и число золотых
слитков N. Следующая строка содержит N чисел, задающих веса слитков. Найдите максимальный вес золота, который можно
унести в рюкзаке. Не разрешается брать часть слитка.
"""


def knapsack_td(w, n, weight, cost):
    """
    D[w - w_i] уже может не подойти, так как там уже может лежать i-й предмет.
    Новые подзадачи:
    D[w][i] - максимальная стоимость рюкзака вместимости w, если разрешено использовать первые i предметов
    """
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


# O(N * W)
def knapsack__bu(w, n, weight, cost):
    d = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1]
            if weight[j - 1] <= i:
                d[i][j] = max(d[i][j], d[i - weight[j - 1]][j - 1] + cost[j - 1])
    return d[w][n]


def golden_knapsack(w, n, weight):
    d = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j - 1]
            if weight[j - 1] <= i:
                d[i][j] = max(d[i][j], d[i - weight[j - 1]][j - 1] + weight[j - 1])
    return d[w][n]
