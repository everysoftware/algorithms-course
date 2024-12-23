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

from enum import Enum, auto
from typing import Any

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


def _ed_rec(a: str, b: str, m: int, n: int) -> int:
    # Если первая строка пуста, то расстояние редактирования равно длине второй строки
    if m == 0:
        return n

    # Если вторая строка пуста, то расстояние редактирования равно длине первой строки
    if n == 0:
        return m

    # Если последние символы строк совпадают, то они игнорируются и рекурсия продолжается для оставшихся строк
    if a[m - 1] == b[n - 1]:
        return _ed_rec(a, b, m - 1, n - 1)

    # Если последние символы строк не совпадают, то рассматриваются все три операции на последнем символе первой строки,
    # рекурсивно вычисляется минимальное значение и к нему добавляется 1
    return 1 + min(
        _ed_rec(a, b, m, n - 1),  # Вставка
        _ed_rec(a, b, m - 1, n),  # Удаление
        _ed_rec(a, b, m - 1, n - 1),  # Замена
    )


def ed_rec(a: str, b: str) -> int:
    """
    Вычисляет расстояние редактирования методом рекурсии.
    Сложность O(3^(N + M)), где N и M - длины строк.
    """
    return _ed_rec(a, b, len(a), len(b))


def _ed_dp(n: int, m: int, a: str, b: str) -> list[list[int]]:
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
            if a[i - 1] == b[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(
                    distance[i - 1][j],  # Удаление
                    distance[i][j - 1],  # Вставка
                    distance[i - 1][j - 1],  # Замена
                )

    return distance


def ed_dp(a: str, b: str) -> int:
    """Вычисляет расстояние редактирования методом динамического программирования. Сложность O(NM)"""
    n, m = len(a), len(b)
    distance = _ed_dp(n, m, a, b)

    return distance[n][m]


class EditOperation(Enum):
    DELETE = auto()
    INSERT = auto()
    REPLACE = auto()


def get_path(
    n: int, m: int, a: str, b: str, distance: list[list[int]]
) -> list[Any]:
    """
    Восстановление пути. Сложность O(N + M)
    """
    path: list[Any] = []
    i, j = n, m

    while i > 0 and j > 0:
        # Совпадение
        if a[i - 1] == b[j - 1]:
            i -= 1
            j -= 1
        else:
            # Замена
            if distance[i][j] == distance[i - 1][j - 1] + 1:
                path.append((EditOperation.REPLACE, i, a[i - 1], b[j - 1]))
                i -= 1
                j -= 1
            # Вставка
            elif distance[i][j] == distance[i][j - 1] + 1:
                path.append((EditOperation.INSERT, i + 1, b[j - 1], -1))
                j -= 1
            # Удаление
            else:
                path.append((EditOperation.DELETE, i, a[i - 1], -1))
                i -= 1

    # Если осталась строка A, удаляем лишние символы
    while i > 0:
        path.append((EditOperation.DELETE, i, a[i - 1], -1))
        i -= 1

    # Если осталась строка B, вставляем недостающие символы
    while j > 0:
        path.append((EditOperation.INSERT, 1, b[j - 1], -1))
        j -= 1

    return path[::-1]


def edit_path(
    a: str, b: str
) -> tuple[int, list[tuple[EditOperation, int, str, str]]]:
    """Путь редактирования. Сложность O(NM)"""
    n, m = len(a), len(b)
    distance = _ed_dp(n, m, a, b)

    return distance[n][m], get_path(n, m, a, b, distance)


def editing(a: str, words: list[str]) -> tuple[int, list[str]]:
    """
    Вычисляет расстояние редактирования между строкой a и каждой строкой из списка words.
    Возвращает список строк, расстояние редактирования которых минимально.
    Сложность O(QNM), где N - длина строки a, M - длина самой длинной строки из списка words.
    """
    distances = [ed_dp(a, word) for word in words]
    min_distance = min(distances)
    result = [
        word
        for word, distance in zip(words, distances)
        if distance == min_distance
    ]

    return min_distance, result
