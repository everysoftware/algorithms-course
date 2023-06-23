class DirectAddressMap:
    def __init__(self, n):
        self.a = [None] * n
        self.n = n

    def add(self, number, name):
        self.a[number] = name

    def get(self, number, default=None):
        if self.a[number] is None:
            return default
        return self.a[number]

    def delete(self, number):
        if self.a[number] is None:
            raise KeyError
        self.a[number] = None
