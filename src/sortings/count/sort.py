
# сортировка подсчётом - O(N + M), M - верхняя граница чисел
def count_sort(a, m):
    n = len(a)
    b = [0] * (m + 1)
    for i in range(n):
        b[a[i]] += 1
    # b[i] = сколько раз i встречается в a
    # составляем массив префиксных сумм (для стабильности сортировки)
    for i in range(1, m + 1):
        b[i] += b[i - 1]
    # b[i] = сколько раз в a встречаются числа меньшие или равные i
    a_sorted = [0] * n
    for i in range(n - 1, -1, -1):
        a_sorted[b[a[i]] - 1] = a[i]
        b[a[i]] -= 1
    return a_sorted


def count_sort_key(a, m, key=None):
    n = len(a)
    b = [0] * (m + 1)
    if key is None:
        keys = a
    else:
        keys = a.copy()
        for i in range(n):
            keys[i] = key(a[i])
    for i in range(n):
        b[keys[i]] += 1
    for i in range(1, m + 1):
        b[i] += b[i - 1]
    a_sorted = [0] * n
    for i in range(n - 1, -1, -1):
        a_sorted[b[keys[i]] - 1] = a[i]
        b[keys[i]] -= 1
    return a_sorted
