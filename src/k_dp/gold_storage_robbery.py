# O(NW)
def rob_gold_storage_dp(w: int, weight: list[int]) -> int:
    # dp[i] - максимальный вес рюкзака вместимости i
    dp = [0] * (w + 1)
    # Перебираем все предметы.
    for item_weight in weight:
        for i in range(w, item_weight - 1, -1):
            dp[i] = max(dp[i], dp[i - item_weight] + item_weight)
    return dp[w]


# O(NW)
def rob_gold_storage_dp2(w: int, weight: list[int]) -> int:
    n = len(weight)
    # max_weight[i][j] - максимальный вес рюкзака вместимости i, если разрешено использовать первые j предметов
    dp = [[0] * (n + 1) for _ in range(w + 1)]
    for i in range(1, w + 1):
        for j in range(1, n + 1):
            weight_without_item = dp[i][j - 1]
            item_weight = weight[j - 1]
            dp[i][j] = weight_without_item
            # Если предмет помещается в рюкзак.
            if item_weight <= i:
                weight_with_item = dp[i - item_weight][j - 1] + item_weight
                dp[i][j] = max(weight_without_item, weight_with_item)
    return dp[w][n]
