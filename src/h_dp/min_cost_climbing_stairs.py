# O(n)
def min_cost_climbing_stairs(a: list[int]) -> int:
    n = len(a)
    # dp[i] - минимальная сумма до i-й ступеньки
    dp = [0] * n
    dp[0], dp[1] = a[0], a[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + a[i]
    return min(dp[n - 1], dp[n - 2])
