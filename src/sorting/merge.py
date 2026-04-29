# O(n + m)
def merge(a: list[int], b: list[int]) -> list[int]:
    # Проходим по обоим спискам и добавляем наименьший элемент в объединенный список.
    # Если один из списков закончился, добавляем оставшиеся элементы другого списка.
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


# O(n + m)
def merge_inplace(a: list[int], n: int, b: list[int], m: int) -> None:
    # Проходим по обоим спискам и добавляем наименьший элемент в объединенный список.
    # Если один из списков закончился, добавляем оставшиеся элементы другого списка.
    i = n - 1
    j = m - 1
    k = n + m - 1
    while i >= 0 and j >= 0:
        if a[i] >= b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    while j >= 0:
        a[k] = b[j]
        j -= 1
        k -= 1
