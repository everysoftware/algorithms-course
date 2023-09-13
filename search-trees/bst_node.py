class BSTNode:
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'{type(self).__name__}(K: {self.key}, V: {self.value}, P: {parent}, L: {left}, R: {right})'

    def __repr__(self):
        return str(self)

    def find(self, key):
        return find(self, key)

    def insert(self, key, value=None):
        return insert(self, key, value)

    def in_order(self):
        return in_order(self)

    def print(self, node=None):
        print_recursive(self if node is None else node)

    def print_d(self, node=None):
        print_d(self if node is None else node)

    def maximum(self):
        return maximum(self)

    def minimum(self):
        return minimum(self)

    def next_element(self):
        return next_element(self)

    def prev_element(self):
        return prev_element(self)

    def delete(self, key):
        return delete(self, key)

    def root(self):
        return get_root(self)

    def is_leaf(self):
        return is_leaf(self)

    def merge(self, node):
        return merge(self, node)

    def split(self, key):
        return split(self, key)


def print_d(node):
    if node is None:
        print('Empty node')
        return
    print('*** Information ***')
    print(f'Root: {node}')
    print('Tree nodes:')
    print(*node.in_order(), sep='\n')
    print('Tree:')
    node.print()
    print('********************')


def get_root(node):
    while node.parent is not None:
        node = node.parent
    return node


def clear_parent(*nodes):
    for node in nodes:
        if node is not None:
            node.parent = None


def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node
    elif node.key > key:
        return find(node.left, key)
    else:
        return find(node.right, key)


def insert(node, key, value=None, parent=None):
    if node is None and isinstance(parent, BSTNode):
        return type(parent)(key, value, parent)
    elif node is None and not isinstance(parent, BSTNode):
        return None
    if node.key > key:
        node.left = insert(node.left, key, value, node)
    elif node.key < key:
        node.right = insert(node.right, key, value, node)
    return node


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node] + in_order(node.right)


def print_recursive(node, level=0):
    if node is not None:
        if node.left is node or node.right is node:
            raise RecursionError
        print_recursive(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        print_recursive(node.right, level + 1)


def maximum(node):
    if node is None:
        return None
    while node.right:
        node = node.right
    return node


def minimum(node):
    if node is None:
        return None
    while node.left:
        node = node.left
    return node


def next_element(node):
    if node is None:
        return None
    if node.right is not None:
        return minimum(node.right)
    # Идем наверх, пока идём направо.
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
    # Идем наверх, пока идём налево.
    parent = node.parent
    while parent is not None and parent.left is node:
        node = parent
        parent = parent.parent
    return parent


def delete(node, key):
    if node is None:
        return None
    if node.key == key:
        if node.left is None or node.right is None:
            child = node.right if node.left is None else node.left
            if child is not None:
                child.parent = node.parent
            if node.parent is not None:
                if node.parent.left is node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            node = child
        else:
            swap_node = prev_element(node)
            node.key = swap_node.key
            node.value = swap_node.value
            node.left = delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = delete(node.left, key)
    else:
        node.right = delete(node.right, key)
    return node


def is_leaf(node):
    return node.left is None and node.right is None


# Склейка при известной идеально подходящей вершине tree: (node1 < tree <= node2).
def merge_with_root(left, right, root):
    root.left = left
    root.right = right
    if left is not None:
        left.parent = root
    if right is not None:
        right.parent = root
    return root


def merge(left, right):
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left
    new_root = maximum(left)
    left = delete(left, new_root.key)
    clear_parent(new_root)
    return merge_with_root(left, right, new_root)


def split(node, key):
    if node is None:
        return None, None
    if node.key > key:
        """
        Корень и всё его правое поддерево должно отправиться во 2 часть ответа, потому что там всё больше чем key.
        В левом же поддереве могут быть ключи как <= key, так и > key, поэтому его мы продолжаем резать.
        После этого левая часть этого рекурсивного разреза - это сразу первая часть нашего ответа, 
        а чтобы получить вторую часть - мы сливаем правую часть дерева с правой частью рекурсивного разреза.
        """
        left, temp = split(node.left, key)
        clear_parent(temp, node.right)
        right = merge_with_root(temp, node.right, node)
    else:
        """
        Корень и всё его левое поддерево должны отправиться в 1 часть ответа, потому что там всё меньше или равно key.
        В правом же поддереве могут быть как ключи <= key, так и > key, поэтому продолжаем резать.
        После этого правая часть разреза сразу идёт как 2 часть ответа, а чтобы получить первую, сливаем левые части.
        """
        temp, right = split(node.right, key)
        clear_parent(node.left, temp)
        left = merge_with_root(node.left, temp, node)
    clear_parent(left, right)
    return left, right
