from abc import ABC, abstractmethod


class DSU(ABC):
    def __init__(self, n: int) -> None:
        self.n = n

    @abstractmethod
    def make_set(self, x: int) -> None:
        """Создать одноэлементное множество {x}"""
        ...

    @abstractmethod
    def find(self, x: int) -> int:
        """Выдать ID множества, содержащего {x}"""
        ...

    @abstractmethod
    def union(self, x: int, y: int) -> None:
        """Объединить множества, содержащие {x} и {y}"""
        ...


class ArrayDSU(DSU):
    """
    Система непересекающихся множеств на массиве.

    ID множества - минимальный элемент в нем.

    s1 = {9, 3, 2, 4, 7}, s2 = {5}, s3 = {6, 1, 8}

    smallest[i] - ID множества, которому принадлежит элемент i:
    smallest[9] = 2, smallest[3] = 2, smallest[2] = 2, smallest[4] = 2, smallest[7] = 2, smallest[5] = 5,
    smallest[6] = 1, smallest[1] = 1, smallest[8] = 1.

    smallest = [0, 1, 2, 2, 2, 5, 1, 2, 1, 2]
    """

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.smallest = [0] * (self.n + 1)

    # O(1)
    def make_set(self, x: int) -> None:
        self.smallest[x] = x

    # O(1)
    def find(self, x: int) -> int:
        return self.smallest[x]

    # O(N)
    def union(self, x: int, y: int) -> None:
        x_id = self.find(x)
        y_id = self.find(y)
        if x_id == y_id:
            return
        new_id = min(x_id, y_id)
        for i in range(1, self.n + 1):
            if self.smallest[i] in {x_id, y_id}:
                self.smallest[i] = new_id


class ForestDSU(DSU):
    """
    Система непересекающихся множеств на лесе корневых деревьев.

    ID множества - корень дерева.

    s1 = {9, 3, 2, 4, 7}, s2 = {5}, s3 = {6, 1, 8}

    parent[i] - родитель элемента i в дереве.

    union(9, 3) : ранги равны => подвешиваем 9 к 3
    union(3, 2) : rank[3] > rank[2] => подвешиваем 2 к 3
    union(2, 4) : rank[2] = rank[3] > rank[4] => подвешиваем 4 к 3
    union(4, 7) : rank[4] = rank[3] > rank[7] => подвешиваем 7 к 3
    union(6, 1) : ранги равны => подвешиваем 6 к 1
    union(1, 8) : rank[1] > rank[8] => подвешиваем 8 к 1

    Множество s1 (корень 3):
       3
     / | | \
    9  2  4  7

    Множество s2 (корень 5):
    5

    Множество s3 (корень 1):
       1
      / \
     6   8

    parent = [0, 1, 3, 3, 3, 5, 1, 3, 1, 3]

    rank[i] - ранг элемента i в дереве, который используется при объединении.
    В текущей реализации ранг равен высоте дерева в элементе.

    rank = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    """

    def __init__(self, n: int) -> None:
        super().__init__(n)
        self.parent = [0] * (self.n + 1)
        self.rank = [0] * (self.n + 1)

    # O(1)
    def make_set(self, x: int) -> None:
        self.parent[x] = x
        self.rank[x] = 0

    # O(log N)
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return self.parent[x]

    # O(log N)
    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # Более низкое подвешиваем к более высокому, чтобы не увеличивать глубину дерева
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root

            # При одинаковой высоте деревьев подвешиваем к одному из них, а его высоту увеличиваем на единицу
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1


class CompressedForestDSU(ForestDSU):
    """
    Система непересекающихся множеств на лесе корневых деревьев с использованием сжатия путей.
    ID множества - корень дерева.

    Отличия от ForestDSU:
    - При поиске корня дерева для элемента i, мы не только находим корень, но и "подвешиваем" все элементы на пути от i
    до корня непосредственно к корню.
    - Это позволяет значительно ускорить последующие операции find для этих элементов, так как они будут находиться на
    уровне 1 от корня.

    Побочный эффект:
    - rank[i] перестает хранить точную высоту элемента i в дереве, а ставится верхней оценкой все еще актуальной при
    объединении.
    """

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
