def max_robot_sum(coins: list[list[int]]) -> int:
    m, n = len(coins), len(coins[0])
    dp = [[[-(10**20)] * 3 for _ in range(n)] for _ in range(m)]
    for k in range(3):
        dp[0][0][k] = 0 if coins[0][0] < 0 and k > 0 else coins[0][0]
    for i in range(m):
        for j in range(n):
            for k in range(3):
                if i == 0 and j == 0:
                    continue
                gain = coins[i][j]
                if i > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + gain)
                    if k > 0 and gain < 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                if j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + gain)
                    if k > 0 and gain < 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1])
    return dp[-1][-1][-1]
