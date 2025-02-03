# O(n)
def prizes_hard(prize_positions: list[int], k: int) -> int:
    n = len(prize_positions)
    # Максимальное число призов до i-й позиции
    dp = [0] * n
    low, ans = 0, 0
    for high in range(n):
        # Сдвигаем левый указатель, пока не удовлетворим условие
        while prize_positions[high] - prize_positions[low] > k:
            low += 1
        # Считаем число призов в текущем отрезке
        curr = high - low + 1
        # Обновляем максимальное число призов
        dp[high] = max(dp[high - 1] if high > 0 else 0, curr)
        # Сочетаем с лучшим отрезком до текущего отрезка
        ans = max(ans, (dp[low - 1] if low > 0 else 0) + curr)
    return ans
