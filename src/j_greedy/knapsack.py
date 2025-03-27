# O(n log n)
def greedy_knapsack(w: int, items: list[tuple[int, int]]) -> float:
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    # На каждом шаге берём максимальный предмет по удельной стоимости (стоимости предмета за кг).
    max_cost = 0.0
    for cost, weight in items:
        # Если груз влезает, берём его целиком.
        if weight <= w:
            max_cost += weight * (cost / weight)
            w -= weight
        # Если груз не влезает, берём его часть.
        else:
            max_cost += w * (cost / weight)
            break
    return max_cost
