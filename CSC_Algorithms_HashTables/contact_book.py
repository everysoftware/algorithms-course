class Map:
    def __init__(self, n):
        self.a = [None] * n
        self.n = n

    def add(self, number, name):
        self.a[number] = name

    def find(self, number):
        if self.a[number] is None:
            raise KeyError
        return self.a[number]

    def delete(self, number):
        if self.a[number] is None:
            raise KeyError
        self.a[number] = None


def contact_book(n, queries):
    d = Map(10_000_000)
    result = []
    for i in range(n):
        if queries[i][0] == 'add':
            d.add(int(queries[i][1]), queries[i][2])
        elif queries[i][0] == 'find':
            try:
                result.append(d.find(int(queries[i][1])))
            except KeyError:
                result.append('not found')
        elif queries[i][0] == 'del':
            try:
                d.delete(int(queries[i][1]))
            except KeyError:
                pass
        else:
            raise NotImplementedError
    return result
