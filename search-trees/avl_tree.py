"""
АВЛ-дерево
"""

from avl_node import AVLNode
from bst import BST


class AVLTree(BST):
    node_type = AVLNode

    def __init__(self, root=None):
        super().__init__(root)

    def order_statistics(self, k):
        return self.root.order_statistics(k)

    def build_from_array(self, arr):
        if arr is None:
            arr = []
        size = len(arr)
        nodes = [self.node_type() for _ in range(size)]
        for i in range(size):
            key, left, right = arr[i]
            nodes[i].key = key
            if left >= 0:
                nodes[i].left = nodes[left]
                nodes[i].left.parent = nodes[i]
            if right >= 0:
                nodes[i].right = nodes[right]
                nodes[i].right.parent = nodes[i]

        if nodes:
            self.root = nodes[0]
            self.root.update_height_recursive()
            self.root.update_size_recursive()
        else:
            self.root = None

        return self
