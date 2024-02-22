"""
https://contest.yandex.ru/contest/32588/problems/C/

Задача: дана искомая строка и несколько строк для поиска. Необходимо найти такие все строки, из которых
можно получить искомую с помощью минимально возможного набора операций удаления символа, добавления символа
или замены символа.
Ответом является список строк (удовлетворяющих условию выше) в том же порядке, что и во входных данных.

Формат ввода
В первой строке ввода - искомая строка до перевода строки.
Во второй строке находится единственное число n - количество потенциальных кандидатов для поиска
Далее идут n строк, каждая из которых содержит кандидата для поиска. В последней строке символа перевода
строки нет.

Формат вывода
В качестве вывода нужно предоставить следующую информацию:

Первая строка - заголовок с количеством найденных строк.
Вторая строка - заголовок с минимальным количеством операций для трансформации исходной строки в найденные
(или наоборот).
Далее идут k строк, каждая из которых соответствует одному из кандидатов с указанным числом операций.
В последней строке символ перевода строки отсутствует.

Пример
Ввод
whiskbroom
9
congratulatory
frissell
carpers
scatters
almuerzo
igneous
screenage
polderboy
studentship
Вывод
Most similar words = 4
Minimal operations needed = 8
frissell
almuerzo
igneous
polderboy

Задача сводится к поиску расстояния редактирования исходной строки и кандидатов.
"""

INF = 10**20

"""
Расстояние редактирования (расстояние Левенштейна) - минимальное количество операций вставки, удаления и замены,
необходимое для преобразования одной строки в другую.

Пример: 
A = "kitten", B = "sitting"
Расстояние редактирования = 3

A = "Saturday", B = "Sunday"
Расстояние редактирования = 3
"""


def edit_distance_rec_helper(a: str, b: str, m: int, n: int) -> int:
    # Если первая строка пуста, то расстояние редактирования равно длине второй строки
    if m == 0:
        return n

    # Если вторая строка пуста, то расстояние редактирования равно длине первой строки
    if n == 0:
        return m

    # Если последние символы строк совпадают, то они игнорируются и рекурсия продолжается для оставшихся строк
    if a[m - 1] == b[n - 1]:
        return edit_distance_rec_helper(a, b, m - 1, n - 1)

    # Если последние символы строк не совпадают, то рассматриваются все три операции на последнем символе первой строки,
    # рекурсивно вычисляется минимальное значение и к нему добавляется 1
    return 1 + min(
        edit_distance_rec_helper(a, b, m, n - 1),  # Вставка
        edit_distance_rec_helper(a, b, m - 1, n),  # Удаление
        edit_distance_rec_helper(a, b, m - 1, n - 1),  # Замена
    )


def edit_distance_rec(a: str, b: str) -> int:
    """
    Вычисляет расстояние редактирования методом рекурсии.
    Сложность O(3^(N + M)), где N и M - длины строк.
    """
    return edit_distance_rec_helper(a, b, len(a), len(b))


def get_distance(n: int, m: int, a: str, b: str) -> list[list[int]]:
    """Построение матрицы расстояний методом динамического программирования. Сложность O(NM)"""
    distance = [[INF] * (m + 1) for _ in range(n + 1)]
    """distance[i][j] - расстояние редактирования для строк a[:i] и b[:j]"""

    # Расстояние от пустой строки до строки длины i равно i
    for i in range(n + 1):
        distance[i][0] = i

    # Расстояние от строки длины j до пустой строки равно j
    for j in range(m + 1):
        distance[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = a[i - 1] != b[j - 1]
            distance[i][j] = min(
                distance[i - 1][j] + 1,
                distance[i][j - 1] + 1,
                distance[i - 1][j - 1] + c,
            )

    return distance


def edit_distance_dp(a: str, b: str) -> int:
    """Вычисляет расстояние редактирования методом динамического программирования. Сложность O(NM)"""
    n, m = len(a), len(b)
    distance = get_distance(n, m, a, b)

    return distance[n][m]


def get_path(n: int, m: int, distance: list[list[int]]) -> list[tuple[int, int, int]]:
    """
    Восстановление пути. Сложность O(N + M)

    Принцип работы: чтобы восстановить решение, пойдём обратно от ячейки distance[n - 1][m - 1] к ячейке
    distance[0][0].

    Если distance[i][j] = distance[i - 1][j] + 1, то была произведено удаление
    Если distance[i][j] = distance[i][j - 1] + 1, то было произведена вставка
    Если distance[i][j] = distance[i - 1][j - 1] + isDiff(a[i], b[j]), то было (не)соответствие
    """

    i, j = n - 1, m - 1
    result = []

    while i >= 0 and j >= 0:
        if i > 0 and distance[i][j] == distance[i - 1][j] + 1:
            result.append((0, i - 1, j))
            i -= 1
        elif j > 0 and distance[i][j] == distance[i][j - 1] + 1:
            result.append((1, i, j))
            j -= 1
        else:
            if i > 0 and j > 0 and distance[i][j] == distance[i - 1][j - 1] + 1:
                result.append((2, i, j))
            i -= 1
            j -= 1

    return result[::-1]


def edit_path(a: str, b: str) -> list[tuple[int, int, int]]:
    n, m = len(a), len(b)
    distance = get_distance(n, m, a, b)

    return get_path(n, m, distance)
