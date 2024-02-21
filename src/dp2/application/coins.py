"""
https://contest.yandex.ru/contest/32588/problems/D/

Дана игровая матрица размером n строк и m столбцов, верхняя левая клетка поля имеет координаты (0,0),
а правая нижняя (n-1, m-1). Имеется игровой робот, который изначально находится в клетке (x, y), где
х - номер строки, у - номер столбца игровой матрицы. Робот умеет ходить по игровому полю либо вниз
(номер строки увеличивается на 1), либо вправо (номер столбца увеличивается на 1). Приходя в новую клетку,
робот собирает все монеты, которые там находятся.

Задача - найти самый прибыльный (по количеству собранных монет) путь из стартовой клетки робота в клетку
(n-1, m-1).

Формат ввода
Игровая доска с позицией робота (обозначена S) и количеством монет на каждой клетке. Считаем, что на стартовой
клетке робота монет нет.

Формат вывода
Самый прибыльный путь робота из стартовой клетки в конечную (n-1, m-1). Путь задается в виде последовательности
координат вершин в специальном формате. Если таких путей несколько, то приоритетом является тот, в котором
раньше следует шаг вправо.

Пример
Ввод
2 2
S 1
1 0
Вывод
Path:
(0,0) (0,1) (1,1)
Coins: 1
"""

INF = 10**20


def coins_helper(
    size: tuple[int, int],
    start: tuple[int, int],
    field: list[list[int]],
    current: tuple[int, int],
) -> int:
    i, j = current

    if i == size[0] - 1 and j == size[1] - 1:
        return field[i][j]

    if i >= size[0] or j >= size[1]:
        return -INF

    moves = [(i + 1, j), (i, j + 1)]
    sums = [coins_helper(size, start, field, move) for move in moves]

    return max(sums) + field[i][j]


def coins_recursive(i_start: int, j_start: int, field: list[list[int]]) -> int:
    """Решение с помощью рекурсии. Сложность O(2^(N+M))"""
    size = len(field), len(field[0])
    start = i_start, j_start

    field[i_start][j_start] = 0

    return coins_helper(size, start, field, start)


def coins_cache_helper(
    size: tuple[int, int],
    start: tuple[int, int],
    coins: list[list[int]],
    current: tuple[int, int],
    cache: dict[tuple[int, int], int],
) -> int:
    i, j = current

    if i == size[0] - 1 and j == size[1] - 1:
        return coins[i][j]

    if i >= size[0] or j >= size[1]:
        return -INF

    if current not in cache:
        moves = [(i + 1, j), (i, j + 1)]
        sums = [coins_cache_helper(size, start, coins, move, cache) for move in moves]

        cache[current] = max(sums) + coins[i][j]

    return cache[current]


def coins_cache(i_start: int, j_start: int, coins: list[list[int]]) -> int:
    """Решение с помощью кэширования. Сложность O(NM)"""
    size = len(coins), len(coins[0])
    start = i_start, j_start

    coins[i_start][j_start] = 0

    return coins_cache_helper(size, start, coins, start, {})


def get_coin_sum(
    n: int, m: int, i_start: int, j_start: int, coins: list[list[int]]
) -> list[list[int]]:
    """Построение матрицы ответов. Сложность O(NM)"""
    coin_sum = [[0] * m for _ in range(n)]

    # Ответ в стартовой точке
    coin_sum[i_start][j_start] = 0

    # Заполняем ответы для первого столбца
    for i in range(i_start + 1, n):
        coin_sum[i][j_start] = coin_sum[i - 1][j_start] + coins[i][j_start]

    # Заполняем ответы для первой строчки
    for j in range(j_start + 1, m):
        coin_sum[i_start][j] = coin_sum[i_start][j - 1] + coins[i_start][j]

    # Заполняем ответы для остальных ячеек
    for i in range(i_start + 1, n):
        for j in range(j_start + 1, m):
            coin_sum[i][j] = max(coin_sum[i - 1][j], coin_sum[i][j - 1]) + coins[i][j]

    return coin_sum


def coins_dp(i_start: int, j_start: int, coins: list[list[int]]) -> int:
    """Решение с помощью динамического программирования. Сложность O(NM)"""
    n, m = len(coins), len(coins[0])

    coin_sum = get_coin_sum(n, m, i_start, j_start, coins)
    return coin_sum[-1][-1]


def get_path(
    n: int, m: int, i_start: int, j_start: int, coin_sum: list[list[int]]
) -> list[tuple[int, int]]:
    """Восстановление пути по матрице ответов. Сложность O(N + M)"""
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
        elif coin_sum[i - 1][j] < coin_sum[i][j - 1]:
            j -= 1
        else:
            i -= 1

    moves.append((i_start, j_start))

    return moves[::-1]


def coins_path(
    i_start: int, j_start: int, coins: list[list[int]]
) -> tuple[int, list[tuple[int, int]]]:
    """Решение с восстановлением пути. Сложность O(NM)"""
    n, m = len(coins), len(coins[0])

    coin_sum = get_coin_sum(n, m, i_start, j_start, coins)
    path = get_path(n, m, i_start, j_start, coin_sum)

    return (
        coin_sum[-1][-1],
        path,
    )
