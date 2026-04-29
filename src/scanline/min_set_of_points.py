# O(n log n)
def min_set_of_points(segments: list[tuple[int, int]]) -> list[int]:
    n = len(segments)
    # Сортируем отрезки по правой границе
    segments.sort(key=lambda entry: entry[1])
    i = 0
    # Покрытие точками
    cover = []
    # Пока не покроем все отрезки
    while i < n:
        # Добавляем минимальный конец отрезка в покрытие
        x = segments[i][1]
        cover.append(x)
        # Пропускаем отрезки, покрытые точкой x
        while i < n and segments[i][0] <= x:
            i += 1
    return cover
