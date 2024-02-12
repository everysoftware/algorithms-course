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
