# O(n * m)
def max_robot_path(i_start: int, j_start: int, coins: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    n, m = len(coins), len(coins[0])
    dp = get_dp_table(n, m, i_start, j_start, coins)
    path = get_path(n, m, i_start, j_start, dp)
    return (
        dp[n - 1][m - 1],
        path,
    )


# O(n * m)
def get_dp_table(n: int, m: int, i_start: int, j_start: int, coins: list[list[int]]) -> list[list[int]]:
    dp = [[0] * m for _ in range(n)]
    # Ответ в стартовой точке
    dp[i_start][j_start] = 0
    # Заполняем ответы для первого столбца
    for i in range(i_start + 1, n):
        dp[i][j_start] = dp[i - 1][j_start] + coins[i][j_start]
    # Заполняем ответы для первой строчки
    for j in range(j_start + 1, m):
        dp[i_start][j] = dp[i_start][j - 1] + coins[i_start][j]
    # Заполняем ответы для остальных ячеек
    for i in range(i_start + 1, n):
        for j in range(j_start + 1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + coins[i][j]
    return dp


# O(n + m)
def get_path(n: int, m: int, i_start: int, j_start: int, dp: list[list[int]]) -> list[tuple[int, int]]:
    moves = []
    i, j = n - 1, m - 1
    while i > i_start or j > j_start:
        moves.append((i, j))
        # Если мы в верхней строке, двигаемся только влево
        if i == i_start:
            j -= 1
        # Если мы в левом столбце, двигаемся только вверх
        elif j == j_start:
            i -= 1
        # Иначе выбираем клетку с большим количеством монет
        elif dp[i - 1][j] < dp[i][j - 1]:
            j -= 1
        else:
            i -= 1
    moves.append((i_start, j_start))
    return moves[::-1]
