# O(n * m * k^2)
def box_filter_naive(image: list[list[int]], k: int = 1) -> list[list[int]]:
    n, m = len(image), len(image[0])
    blurred_image = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            # Размытие пикселя
            total = 0
            count = 0
            for di in range(-k, k + 1):
                for dj in range(-k, k + 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        total += image[ni][nj]
                        count += 1
            blurred_image[i][j] = total // count
    return blurred_image


# o(n*m)
def box_filter_ps(image: list[list[int]], k: int = 1) -> list[list[int]]:
    n, m = len(image), len(image[0])
    prefix_sums = [[0] * (m + 1) for _ in range(n + 1)]
    blurred_image = [[0] * m for _ in range(n)]
    # Вычисление префиксных сумм
    for i in range(n):
        for j in range(m):
            prefix_sums[i + 1][j + 1] = image[i][j] + prefix_sums[i][j + 1] + prefix_sums[i + 1][j] - prefix_sums[i][j]
    # Размытие изображения
    for i in range(n):
        for j in range(m):
            # Координаты начала и конца прямоугольника
            x1, y1 = max(0, i - k), max(0, j - k)
            x2, y2 = min(n, i + k + 1), min(m, j + k + 1)
            # Вычисление суммы и количества пикселей
            total = prefix_sums[x2][y2] - prefix_sums[x1][y2] - prefix_sums[x2][y1] + prefix_sums[x1][y1]
            count = (x2 - x1) * (y2 - y1)
            blurred_image[i][j] = total // count
    return blurred_image
