from bisect import bisect_left


"""
НВП - Наибольшая возрастающая подпоследовательность
LIS - Longest Increasing Subsequence
"""


# O(N^2)
# Пусть D[i] - длина НВП, заканчивающейся в A[i]
# Тогда D[i] = max(D[j]: j < i and A[j] < A[i]) + 1
def lis_length(a):
    n = len(a)
    if n <= 1:
        return n
    d = [1] * n  # длина НВП, заканчивающейся в i-м элементе
    # перебираем концы подпоследовательности
    for i in range(n):
        # в d[i] лежит 1 как подп-ть из самого i-го элемента
        # перебираем возможных предков i-го элемента (кандидаты на предыдущий эл-т под-пти)
        for j in range(i):
            # кандидат a[j] должен быть меньше нашего элемента, а также
            # если приписать к под-пти d[j] наш элемент, то ответ должен быть больше,
            # чем текущий ответ в i-ом элементе
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    # находим максимум
    ans = max(d)
    return ans


def lis(a):
    n = len(a)
    if n <= 1:
        return [] if n == 0 else [0]
    d = [1] * n  # длина НВП, заканчивающейся в i-м элементе
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)  # длина НВП
    s = [-1] * ans  # путь
    i = n - 1  # индекс в s
    # еcли ans = 5, то мы будем сканировать массив d справа налево
    # до 1-й 5, потом до 1-й 4, потом до 1-й 3 и так далее
    # 5 4 3 2 1
    while i >= 0 and ans >= 0:
        if d[i] == ans:
            ans -= 1
            s[ans] = i
        i -= 1
    return s


# ещё один способ восстановления пути
def lis2(a):
    n = len(a)
    if n <= 1:
        return [] if n == 0 else [0]
    d = [1] * n  # длина НВП, заканчивающейся в i-м элементе
    prev = [-1] * n  # предыдущий эл-т НВП, заканчивающейся в i-м элементе
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j
    # находим индекс конца НВП
    n = len(d)
    ans = 0
    k = 0
    for i in range(1, n):
        if d[i] > d[k]:
            k = i
            ans = d[i]
    # идём назад по предкам (делаем обратный ход)
    s = [-1] * ans
    j = ans - 1
    while k >= 0:
        s[j] = k
        j -= 1
        k = prev[k]
    return s



# НВП - O(NlogN)
def lis_length_improved(a):
    n = len(a)
    if n <= 1:
        return n
    tail = [0] * n  # tail[i] = последний элемент НВП длины i + 1
    tail[0] = a[0]  # НВП длины 1
    k = 1  # длина НВП
    for i in range(1, n):
        # Если текущим элементом можно продолжить последовательность длины k - 1, мы продолжаем
        if a[i] > tail[k - 1]:
            tail[k] = a[i]
            k += 1
        # Иначе мы ищем, в п-ть какой длины можно засунуть текущий элемент и засовываем
        else:
            tail[bisect_left(tail, a[i], 0, k - 1)] = a[i]
    return k


def lis_improved(a):
    n = len(a)
    if n <= 1:
        return [] if n == 0 else [0]
    tail = [0] * n  # tail[i] = индекс последнего элемента НВП длины i + 1
    prev = [-1] * n  # prev[i] = индекс предыдущего элемента НВП, которая заканчивается в i-м элементе
    tail[0] = 0
    k = 1
    for i in range(1, n):
        if a[i] > a[tail[k - 1]]:
            # сохраняем, к какому элементу мы добавляем текущий
            prev[i] = tail[k - 1]
            tail[k] = i
            k += 1
        else:
            # находим индекс элемента, который меньше или равен нашему
            idx = lower_bound(tail, a[i], 0, k - 1, key=lambda x: a[x])
            prev[i] = tail[idx - 1]
            tail[idx] = i
    return get_path(tail, prev, k)

