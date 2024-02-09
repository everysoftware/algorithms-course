class MaxDSU:
    def __init__(self, lst):
        self.parent = list(range(len(lst)))
        self.maximum = lst.copy()
        self.rank = [0] * len(lst)
        self.curr_max = max(self.maximum)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Объединяет множества
        :param i: ID первого множества
        :param j: ID второго множества
        :return: ничего
        """
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.maximum[i_id] += self.maximum[j_id]
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
            self.maximum[j_id] += self.maximum[i_id]
        self.curr_max = max(self.curr_max, self.maximum[i_id], self.maximum[j_id])

