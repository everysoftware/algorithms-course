# сортировка кучей - O(NlogN)
import heapq


def heap_sort(a: list[int]) -> list[int]:
    n = len(a)
    h: list[int] = []
    for i in range(n):
        heapq.heappush(h, a[i])
    return [heapq.heappop(h) for _ in range(n)]


# просеивание вниз - O(logN)
def sift_down(a: list[int], size: int, i: int) -> None:
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
def build_heap(a: list[int], size: int) -> None:
    for i in range(size // 2, -1, -1):
        sift_down(a, size, i)


# сортировка кучей на месте - O(NlogN)
def heap_sort_inplace(a: list[int]) -> None:
    n = len(a)
    build_heap(a, n)
    size = n
    for _i in range(n, 1, -1):
        a[size - 1], a[0] = a[0], a[size - 1]
        size -= 1
        sift_down(a, size, 0)
