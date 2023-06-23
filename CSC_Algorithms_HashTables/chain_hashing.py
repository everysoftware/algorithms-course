from collections import deque


class StringHashTable:
    def __init__(self, m):
        self.d = {}
        self.m = m

    def h(self, s):
        p = 1_000_000_007
        x = 263
        result = 0
        for i, c in enumerate(s):
            result += (ord(c) * (x ** i)) % p
        result %= p
        result %= self.m
        return result

    def add(self, string):
        key = self.h(string)
        if key not in self.d:
            self.d[key] = deque()
        if string not in self.d[key]:
            self.d[key].appendleft(string)

    def delete(self, string):
        key = self.h(string)
        if key not in self.d:
            raise KeyError
        try:
            self.d[key].remove(string)
        except ValueError:
            raise KeyError

    def find(self, string):
        key = self.h(string)
        return key in self.d and string in self.d[key]


def chain_hashing(m, n, queries):
    s = StringHashTable(m)
    result = []
    for query in queries:
        command = query[0]
        if command == 'add':
            s.add(query[1])
        elif command == 'del':
            try:
                s.delete(query[1])
            except KeyError:
                pass
        elif command == 'find':
            result.append('yes' if s.find(query[1]) else 'no')
        elif command == 'check':
            key = int(query[1])
            result.append(' '.join(s.d.get(key, '')))
        else:
            raise NotImplementedError
    return result
