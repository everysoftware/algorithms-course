"""
АВЛ-дерево - это сбалансированное двоичное дерево поиска.

Для любого узла АВЛ-дерева высота его правого поддерева отличается от высоты левого поддерева не более чем на единицу.
"""


from bst import BSTNode


class AVLNode(BSTNode):
    def __init__(self, key=None, parent=None, left=None, right=None):
        super().__init__(key, parent, left, right)
        self.height = 1

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'Node(key: {self.key}, height: {self.height}, parent: {parent}, left: {left}, right: {right})'

    def __repr__(self):
        return str(self)

    def add(self, key):
        return add(self, key)

    def delete(self, key):
        return delete(self, key)


def height(node):
    if node is None:
        return 0
    return node.height


# Индикатор сбалансированности:
# если get_balance(x) <= 1, то всё хорошо.
# если get_balance(x) = -2, значит, слева высота больше, поэтому балансируем дерево вправо.
# если get_balance(x) = 2, значит, больше высота справа, и нужно балансировать дерево влево.
def get_balance(node):
    if node is None:
        return 0
    return height(node.right) - height(node.left)


def is_balanced(node):
    return abs(get_balance(node)) <= 1


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def right_rotate(node):
    # node = 4
    node_parent = node.parent  # ...
    a = node.left  # 2
    b = a.right  # 3
    a.right = node
    node.parent = a
    node.left = b
    if b is not None:
        b.parent = node
    a.parent = node_parent
    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a
    update_height(node)
    update_height(a)


def left_rotate(node):
    # node = 4
    node_parent = node.parent  # ...
    a = node.right  # 2
    b = a.left  # 3
    a.left = node
    node.parent = a
    node.right = b
    if b is not None:
        b.parent = node
    a.parent = node_parent
    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a
    update_height(node)
    update_height(a)


def balance(node):
    k = get_balance(node)
    if k == -2:
        if get_balance(node.left) == 1:
            left_rotate(node.left)
        right_rotate(node)
        return True
    elif k == 2:
        if get_balance(node.right) == -1:
            right_rotate(node.right)
        left_rotate(node)
        return True
    return False


def add(node, key):
    if node is None:
        return False
    if node.key > key:
        if node.left is None:
            node.left = AVLNode(key, node)
            result = True
        else:
            result = add(node.left, key)
    else:
        if node.right is None:
            node.right = AVLNode(key, node)
            result = True
        else:
            result = add(node.right, key)

    update_height(node)

    if not is_balanced(node):
        print(f'Addition {key} requires balancing {node}')
        print('Before balancing:')
        node.root().print()
        balance(node)
        print('After balancing:')
        node.root().print()

    return result


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
            # корень с 1 листом
            elif node.parent is None and child is not None:
                node.swap(child)  # пользуемся свойством АВЛ :)
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

    update_height(node)
    balance(node)

    return result


def height_recursive(node):
    if node is None:
        return 0
    return 1 + max(height_recursive(node.left), height_recursive(node.right))


def update_height_recursive(node):
    if node is None:
        return
    node.height = height_recursive(node) if node.parent is None else (node.parent.height - 1)
    update_height_recursive(node.left)
    update_height_recursive(node.right)


def make_avl(arr):
    if arr is None:
        arr = []
    size = len(arr)
    tree = [AVLNode() for _ in range(size)]
    for i in range(size):
        key, left, right = arr[i]
        tree[i].key = key
        if left >= 0:
            tree[i].left = tree[left]
            tree[i].left.parent = tree[i]
        if right >= 0:
            tree[i].right = tree[right]
            tree[i].right.parent = tree[i]
    root = tree[0] if tree else None
    update_height_recursive(root)
    return root
