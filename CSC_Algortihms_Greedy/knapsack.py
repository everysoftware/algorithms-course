"""
Задача о заполнении всего рюкзака вещами максимальной стоимости
(вор в магазине) - O(NlogN)
"""


def knapsack(n: int, v: int, items: list) -> list:
    s = sorted([[w, c / w] for c, w in items], key=lambda x: -x[1])
    result = []
    max_cost = 0
    # на каждом шаге берём максимальный по стоимости за кг предмет
    for w, kg_cost in s:
        # если хватает, то кладём предмет полностью
        if w <= v:
            max_cost += w * kg_cost
            result.append([w, w * kg_cost])
            v -= w
        # иначе берём столько, сколько осталось в рюкзаке места
        else:
            if v > 0:
                max_cost += v * kg_cost
                result.append([w, v * kg_cost])
            break
    return result


