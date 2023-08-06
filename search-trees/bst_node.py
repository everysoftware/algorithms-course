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
        return f'BSTNode(key: {self.key}, parent: {parent}, left: {left}, right: {right})'

    def __repr__(self):
        return str(self)

    def find(self, key):
        return find(self, key)

    def add(self, key):
        return add(self, key)

    def in_order(self):
        return in_order(self)

    def self_print(self):
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
        return get_root(self)

    def is_leaf(self):
        return is_leaf(self)

    def merge(self, node):
        return merge(self, node)

    def split(self, key):
        return split(self, key)


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


def in_order(node):
    if node is None:
        return []
    return in_order(node.left) + [node.key] + in_order(node.right)


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


def delete_base_case(node):
    if node is None:
        return False
    if node.left is None or node.right is None:
        child = node.right if node.left is None else node.left
        if child is not None:
            child.parent = node.parent
        if node.parent is None:
            # корень
            if child is None:
                return False
            else:
                # чтобы найти новый корень при его обновлении через root()
                node.parent = child
        else:
            # некорневая вершина
            if node.parent.left is node:
                node.parent.left = child
            else:
                node.parent.right = child
    return True


def delete_node(node, target):
    if node is None:
        return False
    if node is target:
        if node.left is None or node.right is None:
            print(f'Node found: {node}')
            return delete_base_case(node)
        else:
            swap_node = prev_element(node)
            print(f'Swap node: {swap_node}')
            swap(node, swap_node)
            return delete_node(node.left, target)
    elif node.key > target.key:
        return delete_node(node.left, target)
    else:
        return delete_node(node.right, target)


def delete(node, key):
    if node is None:
        return False
    if node.key == key:
        if node.left is None or node.right is None:
            print(f'Node found: {node}')
            return delete_base_case(node)
        else:
            swap_node = prev_element(node)
            print(f'Swap node: {swap_node}')
            swap(node, swap_node)
            return delete_node(node.left, swap_node)
    elif node.key > key:
        return delete(node.left, key)
    else:
        return delete(node.right, key)


def is_leaf(node):
    return node.left is None and node.right is None


# склейка при известной идеально подходящей вершине tree
# (node1 < tree <= node2)
def merge_with_root(node1, node2, root):
    root.left = node1
    root.right = node2
    if node1 is not None:
        node1.parent = root
    if node2 is not None:
        node2.parent = root
    return root


def merge(node1, node2):
    root = maximum(node1)
    delete_base_case(root)
    node1 = get_root(root)
    # удаление корня меняет его родителя, поэтому приводим в изначальное состояние
    clear_parent(root)
    return merge_with_root(node1, node2, root)


def split(node, key):
    if node is None:
        return None, None
    if node.key > key:
        # Корень и всё его правое поддерево должно отправиться во 2 часть ответа,
        # потому что там всё больше чем key.
        # В левом же поддереве могут быть ключи как <= key, так и > key, поэтому
        # его мы продолжаем резать.
        # После этого левая часть этого рекурсивного разреза - это сразу первая часть
        # нашего ответа, а чтобы получить вторую часть - мы сливаем правую часть дерева
        # с правой частью рекурсивного разреза.
        left, temp = split(node.left, key)
        clear_parent(temp, node.right)
        right = merge_with_root(temp, node.right, node)
    else:
        # Корень и всё его левое поддерево должны отправиться в 1 часть ответа,
        # потому что там всё меньше или равно key.
        # В правом же поддереве могут быть как ключи <= key, так и > key,
        # поэтому продолжаем резать.
        # После этого правая часть разреза сразу идёт как 2 часть ответа,
        # а чтобы получить первую, сливаем левые части.
        temp, right = split(node.right, key)
        clear_parent(node.left, temp)
        left = merge_with_root(node.left, temp, node)
    clear_parent(left, right)
    return left, right


