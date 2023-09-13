"""
Двоичное дерево поиска
"""

from bst_node import BSTNode


class BST:
    node_type = BSTNode

    def __init__(self, root=None):
        self.root = root

    def empty(self):
        return self.root is None

    def key_exists(self, key):
        return self.find(key) is not None

    def print(self):
        if self.root is None:
            print('Empty tree')
        else:
            self.root.print()

    def print_d(self):
        if self.root is None:
            print('Empty tree')
        else:
            self.root.print_d()

    def in_order(self):
        if self.root is None:
            return []
        return self.root.in_order()

    def find(self, key):
        if self.root is None:
            return None
        return self.root.find(key)

    def insert(self, key, value=None):
        self.root = self.node_type(key, value) if self.empty() else self.root.insert(key, value)
        return self.root

    def maximum(self):
        return self.root.maximum()

    def minimum(self):
        return self.root.minimum()

    def split(self, key):
        return self.root.split(key)

    def merge(self, rhs):
        self.root = self.root.merge(rhs)
        return self.root

    def delete(self, key):
        if self.root is None:
            return
        self.root = self.root.delete(key)
        return self.root

    def build_from_array(self, arr):
        if arr is None:
            arr = []
        size = len(arr)
        tree = [self.node_type() for _ in range(size)]
        for i in range(size):
            key, left, right = arr[i]
            tree[i].key = key
            if left >= 0:
                tree[i].left = tree[left]
                tree[i].left.parent = tree[i]
            if right >= 0:
                tree[i].right = tree[right]
                tree[i].right.parent = tree[i]
        self.root = tree[0] if tree else None
        return self
