REHASH_FACTOR = 0.75
EMPTY = 0
ACTIVE = 1
DELETED = 2


class OpenAddressMap:
    class Node:
        def __init__(self, status=EMPTY, key=None, value=None):
            self.status = status
            self.key = key
            self.value = value

        def is_active(self):
            return self.status == ACTIVE

        def is_empty(self):
            return self.status == EMPTY

        def is_deleted(self):
            return self.status == DELETED

        def __str__(self):
            return f"({self.status}, {self.key}, {self.value})"

    def __init__(self, hash_function, cap=8):
        self.data = [self.Node() for _ in range(cap)]
        self.capacity = cap
        self.size = 0
        self.hash_function = hash_function

    def index(self, key):
        i = self.hash_function(key, self.capacity)
        k = 0
        while (
            self.data[i].is_active()
            and self.data[i].key != key
            or self.data[i].is_deleted()
        ) and k < self.capacity:
            i = (i + 1) % self.capacity
            k += 1
        if k >= self.capacity:
            raise KeyError
        return i

    def index_to_add(self, key):
        i = self.hash_function(key, self.capacity)
        k = 0
        while (
            self.data[i].is_active() and self.data[i].key != key
        ) and k < self.capacity:
            i = (i + 1) % self.capacity
            k += 1
        if k >= self.capacity:
            raise KeyError
        return i

    def reserve(self):
        print(f"RESERVE {self.capacity} -> {self.capacity * 2}:")
        old_data = self.data.copy()
        self.capacity *= 2
        self.data = [self.Node() for _ in range(self.capacity)]
        for node in old_data:
            if node.is_active():
                self.data[self.index(node.key)] = node
        print("Old data:")
        for i, x in enumerate(old_data):
            print(f"\t{i}: {x}")
        print("New data:")
        for i, x in enumerate(self.data):
            print(f"\t{i}: {x}")
        print()
        print()

    def add(self, key, value):
        if self.size / self.capacity >= REHASH_FACTOR:
            self.reserve()
        i = self.index_to_add(key)
        print(
            f"ADD {key}={value} (at idx {i} with hash {self.hash_function(key, self.capacity)})"
        )
        if not self.data[i].is_active():
            self.size += 1
        self.data[i] = self.Node(ACTIVE, key, value)

        print(f"Data after addition ({self.size} / {self.capacity}):")
        for i, x in enumerate(self.data):
            print(f"\t{i}: {x}")
        print()
        print()

    def get(self, key, default=None):
        try:
            x = self.data[self.index(key)]
        except KeyError:
            return default
        return x.value if x.key == key else default

    def delete(self, key):
        try:
            print(f"DELETE {key}")
            self.data[self.index(key)].status = DELETED
            print(f"Data after deletion ({self.size} / {self.capacity}):")
            for i, x in enumerate(self.data):
                print(f"\t{i}: {x}")
            print()
            print()
        except KeyError:
            raise
