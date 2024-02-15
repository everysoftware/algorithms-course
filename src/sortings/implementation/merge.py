"""Слияние двух отсортированных массивов."""


def merge(a: list[int], b: list[int]) -> list[int]:
    """
    Слияние двух отсортированных массивов. Сложность O(N + M).
    Принцип работы: проходим по обоим спискам и добавляем наименьший элемент в объединенный список.
    Если один из списков закончился, добавляем оставшиеся элементы другого списка.
    """
    n, m = len(a), len(b)
    res = []
    i = j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < n:
        res.append(a[i])
        i += 1

    while j < m:
        res.append(b[j])
        j += 1

    return res
