class PriorityQueue:
    def __init__(self, arr: list[int] | None = None) -> None:
        self.arr: list[int] = [] if arr is None else arr.copy()
        self.size = len(self.arr)
        self.heapify()

    def swap(self, i: int, j: int) -> None:
        tmp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp

    # просеивание вверх
    def sift_up(self, i: int) -> None:
        # (i - 1) // 2 - индекс родителя i-й вершины
        while i > 0 and self.arr[i] > self.arr[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    # просеивание вниз
    def sift_down(self, i: int) -> None:
        while 2 * i + 1 < self.size:
            # потомки вершины i
            left = 2 * i + 1
            right = 2 * i + 2
            # берём максимум из потомков
            j = left
            if right < self.size and self.arr[right] > self.arr[left]:
                j = right
            # если текущий элемент больше или равен потомка,
            # значит он располагается правильно - выходим
            if self.arr[i] >= self.arr[j]:
                break
            self.swap(i, j)
            i = j

    # превращение массива в кучу
    def heapify(self) -> None:
        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down(i)

    # вставка
    def insert(self, x: int) -> None:
        self.arr.append(x)
        self.sift_up(self.size)
        self.size += 1

    # извлечение максимума
    def extract_max(self) -> int:
        mx = self.arr[0]
        self.swap(0, self.size - 1)
        self.arr.pop()
        self.size -= 1
        self.sift_down(0)
        return mx
