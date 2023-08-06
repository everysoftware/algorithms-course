"""
BST (Binary Search Tree) - двоичное дерево поиска.
В левом поддереве корня находятся вершины, меньшие корня,
а в правом поддереве - большие или равные корню.
"""


from bst_node import BSTNode


class BST:
    def __init__(self, root=None):
        self.root = root

    def self_print(self):
        if self.root is None:
            print('(Empty tree)')
        else:
            self.root.self_print()

    def in_order(self):
        if self.root is None:
            return []
        return self.root.in_order()

    def find(self, key):
        return self.root.find(key)

    def add(self, key):
        result = self.root.add(key)
        self.root = self.root.root()
        return result

    def maximum(self):
        return self.root.maximum()

    def minimum(self):
        return self.root.minimum()

    def split(self, key):
        return self.root.split(key)

    def merge(self, rhs):
        self.root = self.root.merge(rhs)

    def delete(self, key):
        result = self.root.delete(key)
        self.root = self.root.root()
        if not result and self.root.is_leaf():
            self.root = None
            return True
        return result

    def build_from_array(self, arr):
        if arr is None:
            arr = []
        size = len(arr)
        tree = [BSTNode() for _ in range(size)]
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
