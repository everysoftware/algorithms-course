# O(n^2)
def bubble_sort(a: list[int]) -> None:
    n = len(a)
    # Проходим по массиву n раз, на каждом проходе сдвигая максимальный элемент в конец
    # Сортировка называется пузырьковой, так как на каждом проходе максимальный элемент "всплывает".
    for i in range(n):
        # Проходим по массиву от начала до n - i - 1, так как на каждом проходе максимальный элемент
        # уже находится в конце
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


# O(n^2)
def selection_sort(a: list[int]) -> None:
    # Находим минимум, ставим его первым, находим 2-й минимум, ставим его вторым и т. д.
    n = len(a)
    for i in range(n):
        # Ищем минимум в оставшейся части массива
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]


# O(n^2)
def insertion_sort(a: list[int]) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        # Ставим элемент на его место
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
