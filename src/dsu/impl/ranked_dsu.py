
class RankedDSU:
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
