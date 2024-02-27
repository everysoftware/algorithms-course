"""
Авторская задача (И. Стасевич)

Чёрно-белое изображение представляется как матрица пикселей, где значение каждого пикселя может быть от нуля
(чёрный цвет) до 255 (белый цвет).

Box filter - один из алгоритмов в компьютерном зрении, который позволяет размыть изображение.
В этом алгоритме для каждого пикселя записывается значение, равное среднему среди него самого и всех соседей вокруг.
Расстояние до соседей задаётся размером фильтра.

Например, в изображении:

1 4 3 0 7
2 2 5 5 8
3 1 5 6 6
3 3 5 6 7
3 4 4 5 6

Пиксель 1, стоящий на позиции (3, 2) размоется до: (1 + 4 + 3 + 2 + 2 + 5 + 5 + 5 + 6) // 9 = 29 // 9 = 3
при размере фильтра 1.

Дано изображение размера N x N и размер фильтра M. Необходимо размыть изображение.

Формат ввода:
На вход подаётся матрица пикселей изображения размера N x N (1 <= N <= 1000) и размер фильтра M (1 <= M <= 100).

Формат вывода:
Выведите матрицу размытого изображения.

Пример
Ввод
5 3
1 4 3 0 7
2 2 5 5 8
3 1 5 6 6
3 3 5 6 7
3 4 4 5 6
Вывод
2 2 3 4 5
2 2 3 5 5
2 3 4 5 6
2 3 4 5 6
3 3 4 5 6
"""


def box_filter_naive(m: int, image: list[list[int]]) -> list[list[int]]:
    """Прямоугольное размытие изображения. Сложность O(N^2 * M^2)."""
    n = len(image)
    blurred_image = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Размытие пикселя
            total = 0
            count = 0

            for di in range(-m, m + 1):
                for dj in range(-m, m + 1):
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < n:
                        total += image[ni][nj]
                        count += 1

            blurred_image[i][j] = total // count

    return blurred_image


def box_filter_ps(m: int, image: list[list[int]]) -> list[list[int]]:
    """Прямоугольное размытие изображения с использованием префиксных сумм. Сложность O(N^2)."""
    n = len(image)
    prefix_sums = [[0] * (n + 1) for _ in range(n + 1)]
    blurred_image = [[0] * n for _ in range(n)]

    # Вычисление префиксных сумм
    for i in range(n):
        for j in range(n):
            prefix_sums[i + 1][j + 1] = (
                image[i][j]
                + prefix_sums[i][j + 1]
                + prefix_sums[i + 1][j]
                - prefix_sums[i][j]
            )

    # Размытие изображения
    for i in range(n):
        for j in range(n):
            # Координаты начала и конца прямоугольника
            x1, y1 = max(0, i - m), max(0, j - m)
            x2, y2 = min(n, i + m + 1), min(n, j + m + 1)

            # Вычисление суммы и количества пикселей
            total = (
                prefix_sums[x2][y2]
                - prefix_sums[x1][y2]
                - prefix_sums[x2][y1]
                + prefix_sums[x1][y1]
            )
            count = (x2 - x1) * (y2 - y1)
            blurred_image[i][j] = total // count

    return blurred_image
