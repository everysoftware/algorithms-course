"""
Макс-куча
"""


class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.heap_size = 0

    def swap(self, i, j):
        tmp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp

    # просеивание вверх
    def sift_up(self, i):
        # (i - 1) // 2 - индекс родителя i-й вершины
        while i > 0 and self.arr[i] > self.arr[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    # просеивание вниз
    def sift_down(self, i):
        while 2 * i + 1 < self.heap_size:
            # потомки вершины i
            left = 2 * i + 1
            right = 2 * i + 2
            # берём максимум из потомков
            j = left
            if right < self.heap_size and self.arr[right] > self.arr[left]:
                j = right
            # если текущий элемент больше или равен потомка,
            # значит он располагается правильно - выходим
            if self.arr[i] >= self.arr[j]:
                break
            self.swap(i, j)
            i = j

    # вставка
    def insert(self, x):
        self.arr.append(x)
        self.sift_up(self.heap_size)
        self.heap_size += 1

    # извлечение максимума
    def extract_max(self):
        mx = self.arr[0]
        self.swap(0, self.heap_size - 1)
        self.arr.pop()
        self.heap_size -= 1
        self.sift_down(0)
        return mx
