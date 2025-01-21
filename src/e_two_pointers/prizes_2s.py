# O(n)
def prizes_hard(prize_positions: list[int], k: int) -> int:
    n = len(prize_positions)
    # Максимальное число призов на подмассиве prize_positions[:i]
    dp = [0] * (n + 1)
    low, ans = 0, 0
    for high in range(n):
        # Сдвигаем левый указатель, пока не удовлетворим условие
        while prize_positions[high] - prize_positions[low] > k:
            low += 1
        # Считаем число призов в текущем отрезке
        curr = high - low + 1
        # Обновляем максимальное число призов
        dp[high + 1] = max(dp[high], curr)
        # Сочетаем с лучшим отрезком до текущего
        ans = max(ans, dp[low] + curr)
    return ans
