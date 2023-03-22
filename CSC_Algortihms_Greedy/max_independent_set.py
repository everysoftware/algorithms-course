"""
Планирование вечеринки в компании (так, чтобы на ней не было прямого руководителя кого-либо из гостей)
- O(N), N = |tree|
"""


def max_independent_set(tree: dict) -> list:
    t = tree.copy()
    sol = []
    while t:
        # добавляем листья в решения
        [sol.append(i) for v in t.values() for i in v if i not in t]
        # выкидываем листья и их родителей из дерева
        for d in sol:
            t = {k: v for k, v in t.items() if d not in v}
    return sol

