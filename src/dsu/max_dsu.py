class MaxDSU:
    def __init__(self, sizes: list[int]) -> None:
        self.parent = list(range(len(sizes)))
        self.size = sizes.copy()
        self.curr_max = max(self.size)

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # всегда присоединяем меньшее к большему
        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root

        # теперь x_root - корень большей компоненты
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

        # обновляем максимум только по новому корню
        if self.size[x_root] > self.curr_max:
            self.curr_max = self.size[x_root]
