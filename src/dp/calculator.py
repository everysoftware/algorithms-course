# O(n)
def calculator(n: int) -> list[int]:
    # dp[i] - минимальное число операций, чтобы получить из 1 число i
    dp = [10**20] * (n + 1)
    dp[0], dp[1] = 0, 0
    # prev[i] - предыдущее число, из которого мы пришли в i
    prev = [-1] * (n + 1)
    for x in range(1, n + 1):
        moves = [x + 1, 2 * x, 3 * x]
        for i in moves:
            if i <= n and dp[x] + 1 < dp[i]:
                dp[i] = dp[x] + 1
                prev[i] = x
    return get_path(n, prev)


# O(n)
def get_path(n: int, prev: list[int]) -> list[int]:
    path = []
    # Восстанавливаем путь
    while n > 0:
        # Добавляем число в путь
        path.append(n)
        # Переходим к предыдущему числу
        n = prev[n]
    # Возвращаем путь в обратном порядке
    return path[::-1]
