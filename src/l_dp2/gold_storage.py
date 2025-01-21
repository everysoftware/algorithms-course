"""
https://stepik.org/lesson/13259/step/5?unit=3444

Вы собираетесь ограбить хранилище золота.

Формат ввода
Первая строка входа содержит вместимость рюкзака W и число золотых
слитков N. Следующая строка содержит N чисел, задающих веса слитков.

Формат вывода
Найдите максимальный вес золота, который можно
унести в рюкзаке, учитывая, что не разрешается брать часть слитка.

Пример
Ввод
10 3
1 4 8
Вывод
9

Задача является вариацией задачи о рюкзаке.
"""


def gold_storage(w: int, weight: list[int]) -> int:
    """Решает задачу о хранилище золота. Сложность O(NW)"""
    n = len(weight)
    max_weight = [[0] * (n + 1) for _ in range(w + 1)]
    """max_cost[i][j] - максимальный вес рюкзака вместимости i, если разрешено использовать первые j предметов"""

    for i in range(1, w + 1):
        for j in range(1, n + 1):
            weight_without_item = max_weight[i][j - 1]
            item_weight = weight[j - 1]

            max_weight[i][j] = weight_without_item

            # Если предмет помещается в рюкзак
            if item_weight <= i:
                weight_with_item = max_weight[i - item_weight][j - 1] + item_weight
                max_weight[i][j] = max(weight_without_item, weight_with_item)

    return max_weight[w][n]


def gold_storage_enhanced(w: int, weight: list[int]) -> int:
    """Решает задачу о хранилище золота. Сложность O(NW)"""
    max_weight = [0] * (w + 1)
    """max_cost[i] - максимальный вес рюкзака вместимости i, если разрешено использовать все предметы"""

    for item_weight in weight:
        for i in range(w, item_weight - 1, -1):
            max_weight[i] = max(max_weight[i], max_weight[i - item_weight] + item_weight)

    return max_weight[w]
