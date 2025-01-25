# O(n * m)
def edit_distance_dp(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = get_dp_table(a, b)
    return dp[n][m]


def get_dp_table(a: str, b: str) -> list[list[int]]:
    n, m = len(a), len(b)
    # dp[i][j] - расстояние редактирования для строк a[:i] и b[:j]
    dp = [[10**20] * (m + 1) for _ in range(n + 1)]
    # Расстояние от пустой строки до строки длины i равно i
    for i in range(n + 1):
        dp[i][0] = i
    # Расстояние от строки длины j до пустой строки равно j
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Удаление
                    dp[i][j - 1],  # Вставка
                    dp[i - 1][j - 1],  # Замена
                )
    return dp


# O(3^(n + m))
def edit_distance_rec(a: str, b: str) -> int:
    return _edit_distance_rec(a, b, len(a), len(b))


def _edit_distance_rec(a: str, b: str, m: int, n: int) -> int:
    # Если первая строка пуста, то расстояние редактирования равно длине второй строки
    if m == 0:
        return n
    # Если вторая строка пуста, то расстояние редактирования равно длине первой строки
    if n == 0:
        return m
    # Если последние символы строк совпадают, то они игнорируются и рекурсия продолжается для оставшихся строк
    if a[m - 1] == b[n - 1]:
        return _edit_distance_rec(a, b, m - 1, n - 1)
    # Если последние символы строк не совпадают, то рассматриваются все три операции на последнем символе первой строки,
    # рекурсивно вычисляется минимальное значение и к нему добавляется 1
    return 1 + min(
        _edit_distance_rec(a, b, m, n - 1),  # Вставка
        _edit_distance_rec(a, b, m - 1, n),  # Удаление
        _edit_distance_rec(a, b, m - 1, n - 1),  # Замена
    )
