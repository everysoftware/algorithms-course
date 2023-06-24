import random
import heapq


# Сортировка вставками - O(N^2)
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        # ставим элемент на его место
        while j > 0 and a[j] < a[j - 1]:
            temp = a[j]
            a[j] = a[j - 1]
            a[j - 1] = temp
            j -= 1
    return a


#  Сортировка слиянием - O(NlogN)

# O(N + M)
# процедура слияния - первым элементом резульютирующего
# массива будет меньший из первых элементов данных массивов.
# остальные эл-ты заполняются аналогично
def merge(a, b):
    result = []
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    while i < n or j < m:
        if j == m or i < n and a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result


def merge_sort(a, left, right):
    if left < right:
        m = (left + right) // 2
        # производим сливание двух отсортированных кусков
        left_part = merge_sort(a, left, m)
        right_part = merge_sort(a, m + 1, right)
        return merge(left_part, right_part)
    # дошли до того, что сортируем одноэлементный (или пустой) массив
    else:
        return [a[left]] if len(a) > 0 else []


# реализация сортировки слиянием без рекурсии
def iterative_merge_sort(a):
    q = []
    n = len(a)
    for i in range(n):
        q.append([a[i]])
    while len(q) > 1:
        q.append(merge(q.pop(0), q.pop(0)))
    return q.pop(0) if len(q) > 0 else []


# быстрая сортировка - O(NlogN) в ср., O(N^2) в худш.
# называется "быстрой" потому что она реально быстрая
# на практике быстрее merge_sort, несмотря на O(N^2) в худш. случае
# разбиение массива на две части: до опорного и после - O(N)
def partition(a, left, right):
    # в качестве опорного возьмём первый
    x = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[left], a[j] = a[j], a[left]
    return j


def quick_sort(a, left, right):
    if left < right:
        m = partition(a, left, right)
        quick_sort(a, left, m - 1)
        quick_sort(a, m + 1, right)
    return a


def partition3(a, left, right):
    # в качестве опорного возьмём первый
    x = a[left]
    i = left + 1
    lower = left
    upper = right
    while i <= upper:
        if a[i] < x:
            a[i], a[lower] = a[lower], a[i]
            lower += 1
            i += 1
        elif a[i] > x:
            a[i], a[upper] = a[upper], a[i]
            upper -= 1
        else:
            i += 1
    return lower, upper


def quick_sort3(a, left, right):
    if left < right:
        k = (left + right) // 2
        a[left], a[k] = a[k], a[left]
        lower, upper = partition3(a, left, right)
        quick_sort3(a, left, lower - 1)
        quick_sort3(a, upper + 1, right)
    return a


# поиск k-й порядковой статистики (a'[k]) - O(N) в среднем
def random_select(a, left, right, k):
    if left >= right:
        return a[left]
    m = random.randint(left, right)
    x = a[m]
    a[left], a[m] = a[m], a[left]
    lower, upper = partition3(a, left, right)
    if left <= k < lower:
        return random_select(a, left, lower - 1, k)
    elif lower <= k <= upper:
        return x
    else:
        return random_select(a, upper + 1, right, k)


# сортировка выбором - O(N^2)
# находим минимум, ставим его первым, находим 2-й минимум
# ставим его вторым и т. д.
def selection_sort(a):
    n = len(a)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
    return a


# сортировка кучей - O(NlogN)
def heap_sort(a):
    n = len(a)
    h = []
    for i in range(n):
        heapq.heappush(h, (i, a[i]))
    a_sorted = []
    for i in range(n):
        a_sorted.append(heapq.heappop(h)[1])
    return a_sorted


# просеивание вниз - O(logN)
def sift_down(a, size, i):
    while 2 * i + 1 < size:
        # потомки вершины i
        left = 2 * i + 1
        right = 2 * i + 2
        # берём максимум из потомков
        j = left
        if right < size and a[right] > a[left]:
            j = right
        # если текущий элемент больше или равен потомка,
        # значит он располагается правильно - выходим
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j


# построение кучи - O(N)
def build_heap(a, size):
    for i in range(size // 2, -1, -1):
        sift_down(a, size, i)


# сортировка кучей на месте - O(NlogN)
def heap_sort_inplace(a):
    n = len(a)
    build_heap(a, n)
    size = n
    for i in range(n, 1, -1):
        a[size - 1], a[0] = a[0], a[size - 1]
        size -= 1
        sift_down(a, size, 0)
    return a


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


# цифровая сортировка (digit sort/radix sort) - O(D*N), D - макс. число разрядов
def digit_sort(a):
    x_max = max(a) if a else 0
    d = 0
    while x_max > 0:
        d += 1
        x_max //= 10
    a_sorted = a
    p = 1
    for i in range(d):
        a_sorted = count_sort_key(a_sorted, 9, key=lambda x: (x // p) % 10)
        p *= 10
    return a_sorted
