def coin_change(coins: list[int], n: int) -> int:
    # dp[i] - минимальное количество монет для сбора суммы i
    dp = [10**20] * (n + 1)
    dp[0] = 0
    # Перебираем все суммы от 1 до n
    for i in range(1, n + 1):
        # Перебираем все монеты
        for coin in coins:
            # Если монета меньше или равна сумме
            if coin <= i:
                # Пересчитываем dp[i]
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n] if dp[n] != 10**20 else -1
