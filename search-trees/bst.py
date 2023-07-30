"""
BST (Binary Search Tree) - двоичное дерево поиска.
В левом поддереве корня находятся вершины, меньшие корня,
а в правом поддереве - большие или равные корню.
"""


class BSTNode:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'Node(key: {self.key}, parent: {parent}, left: {left}, right: {right})'

    def __repr__(self):
        return str(self)

    def find(self, key):
        return find(self, key)

    def add(self, key):
        return add(self, key)

    def dfs(self):
        return dfs(self)

    def print(self):
        print_recursive(self)

    def maximum(self):
        return maximum(self)

    def minimum(self):
        return minimum(self)

    def swap(self, rhs):
        return swap(self, rhs)

    def next_element(self):
        return next_element(self)

    def prev_element(self):
        return prev_element(self)

    def delete(self, key):
        return delete(self, key)

    def root(self):
        return root(self)

    def is_leaf(self):
        return is_leaf(self)


def root(node):
    while node.parent is not None:
        node = node.parent
    return node


def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif node.key > key:
        return find(node.left, key)
    else:
        return find(node.right, key)


def add(node, key):
    if node is None:
        return False
    if node.key > key:
        if node.left is None:
            node.left = BSTNode(key, node)
            return True
        else:
            return add(node.left, key)
    else:
        if node.right is None:
            node.right = BSTNode(key, node)
            return True
        else:
            return add(node.right, key)


def dfs(node):
    if node is None:
        return []
    return dfs(node.left) + [node.key] + dfs(node.right)


def print_recursive(node, level=0):
    if node is not None:
        print_recursive(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        print_recursive(node.right, level + 1)


def maximum(node):
    if node is None:
        return None
    if node.right is None:
        return node
    return maximum(node.right)


def minimum(node):
    if node is None:
        return None
    if node.left is None:
        return node
    return minimum(node.left)


def swap(lhs, rhs):
    lhs.key, rhs.key = rhs.key, lhs.key


def next_element(node):
    if node is None:
        return None
    # минимум в правом поддереве
    if node.right is not None:
        return minimum(node.right)
    # идем наверх, пока идём направо
    parent = node.parent
    while parent is not None and parent.right is node:
        node = parent
        parent = parent.parent
    return parent


def prev_element(node):
    if node is None:
        return None
    if node.left is not None:
        return maximum(node.left)
    # идем наверх, пока идём налево
    parent = node.parent
    while parent is not None and parent.left is node:
        node = parent
        parent = parent.parent
    return parent


def delete(node, key):
    if node is None:
        return False
    result = True
    if node.key == key:
        print(f'Node found: {node}')
        if node.left is None or node.right is None:
            child = node.right if node.left is None else node.left
            # корень без детей
            if node.parent is None and child is None:
                result = False
            # корень с 1 вершиной
            elif node.parent is None and child is not None:
                swap_node = node.next_element() if child is node.right else node.prev_element()
                node.swap(swap_node)
                result = delete(child, key)
            # некорневой узел с 1 ребенком
            elif child is not None:
                child.parent = node.parent
            if node.parent is not None:
                if node.parent.left is node:
                    node.parent.left = child
                else:
                    node.parent.right = child
        # вершина с двумя детьми
        else:
            swap_node = node.prev_element()
            print(f'Swap node: {swap_node}')
            node.swap(swap_node)
            result = delete(node.left, key)
    elif node.key > key:
        result = delete(node.left, key)
    else:
        result = delete(node.right, key)

    return result


def is_leaf(node):
    return node.left is None and node.right is None


def make_bst(arr):
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
    return tree[0] if tree else None
