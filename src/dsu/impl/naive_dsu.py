class NaiveDSU:
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
