import bisect


# O((n + m)log(n + m))
def count_segments(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    m = len(points)
    # Формируем список событий
    events: list[tuple[int, int, int]] = []
    for x0, x1 in segments:
        # Начало отрезка - вклад в ответ +1
        events.append((x0, 1, 0))
        # Конец отрезка - вклад в ответ -1
        events.append((x1, -1, 0))
    for i, x in enumerate(points):
        # Появление точки - вклад в ответ 0, записываем индекс (он нужен для сохранения порядка в result)
        events.append((x, 0, i))
    # Сортируем события: по возрастанию X координаты, по убыванию вклада в ответ
    events.sort(key=lambda entry: (entry[0], -entry[1]))
    # Считаем ответ. result[i] - ответ для i-й точки
    result = [0] * m
    # Текущий ответ (сколько отрезков пересекает точка)
    count = 0
    for _, contribute, i in events:
        # Если это отрезок, меняем ответ в соответствии с вкладом в него
        if contribute != 0:
            count += contribute
        # Если это точка, то записываем её ответ
        else:
            result[i] = count
    return result


# O(n log n + m log n) = O((n + m) log n)
def count_segments_bisect(segments: list[tuple[int, int]], points: list[int]) -> list[int]:
    # Формируем список начал и концов отрезка
    x0_all, x1_all = [], []
    for x0, x1 in segments:
        x0_all.append(x0)
        x1_all.append(x1)
    # Сортируем события
    x0_all.sort()
    x1_all.sort()
    # Вычисляем ответ
    result = []
    for x in points:
        # Сколько отрезков начинаются в точке x или левее
        high = bisect.bisect_right(x0_all, x)
        # Сколько отрезков заканчиваются строго левее точки x
        low = bisect.bisect_left(x1_all, x)
        # Количество отрезков, пересекающих точку
        count = high - low
        # Добавляем ответ
        result.append(count)
    return result
