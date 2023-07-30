class NaiveHashSet:
    # ID множества - минимальный элемент
    def __init__(self, n):
        self.smallest = [0] * (n + 1)
        self.n = n

    # O(1)
    def make_set(self, i):
        self.smallest[i] = i

    # O(1)
    def find(self, i):
        return self.smallest[i]

    # O(N)
    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        m = min(i_id, j_id)
        for k in range(1, self.n + 1):
            if self.smallest[k] in {i_id, j_id}:
                self.smallest[k] = m


class UnrankedHashSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.n = n

    def make_set(self, i):
        self.parent[i] = i

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        """
        Объединить множества
        :param i: ID первого множества
        :param j: ID второго множества
        :return: ничего
        """
        # лень писать неэффективное объединение
        raise NotImplementedError


class RankedHashSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.rank = [0] * (n + 1)

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


class CompressedHashSet:
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        self.rank = [0] * (n + 1)

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


HashSet = CompressedHashSet
