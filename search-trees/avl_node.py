import bst_node


class AVLNode(bst_node.BSTNode):
    def __init__(self, key=None, parent=None, left=None, right=None):
        super().__init__(key, parent, left, right)
        self.height = 1
        self.size = 1

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'AVLNode(key: {self.key}, height: {self.height}, size: {self.size}, parent: {parent}, left: {left}, ' \
               f'right: {right})'

    def __repr__(self):
        return str(self)

    def add(self, key):
        return add(self, key)

    def delete(self, key):
        return delete(self, key)

    def order_statistics(self, k):
        return order_statistics(self, k)

    def merge(self, node):
        return avl_merge(self, node)

    def split(self, key):
        return avl_split(self, key)

    def update_height_recursive(self):
        update_height_recursive(self)

    def update_size_recursive(self):
        update_size_recursive(self)


def get_height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def update_height_recursive(node):
    if node is None:
        return 0
    node.height = 1 + max(update_height_recursive(node.left), update_height_recursive(node.right))
    return node.height


def get_size(node):
    if node is None:
        return 0
    return node.size


def update_size(node):
    node.size = get_size(node.left) + get_size(node.right) + 1


def update_size_recursive(node):
    if node is None:
        return 0
    node.size = 1 + update_size_recursive(node.left) + update_size_recursive(node.right)
    return node.size


def update_attributes(node):
    update_size(node)
    update_height(node)


# Индикатор сбалансированности:
# если get_balance(x) <= 1, то всё хорошо.
# если get_balance(x) = -2, значит, слева высота больше, поэтому балансируем дерево вправо.
# если get_balance(x) = 2, значит, больше высота справа, и нужно балансировать дерево влево.
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)


def is_balanced(node):
    return abs(get_balance(node)) <= 1


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
    update_attributes(node)
    update_attributes(a)
    return a


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
    update_attributes(node)
    update_attributes(a)
    return a


def balance(node):
    k = get_balance(node)
    possible_new_root = node
    if k == -2:
        if get_balance(node.left) == 1:
            left_rotate(node.left)
        possible_new_root = right_rotate(node)
    elif k == 2:
        if get_balance(node.right) == -1:
            right_rotate(node.right)
        possible_new_root = left_rotate(node)
    return possible_new_root


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

    update_attributes(node)

    if not is_balanced(node):
        print(f'Addition {key} requires balancing {node}')
        print('Before balancing:')
        node.root().self_print()
        balance(node)
        print('After balancing:')
        node.root().self_print()

    return result


def delete_base_case(node):
    result = bst_node.delete_base_case(node)
    update_attributes(node)
    balance(node)
    return result


def delete_node(node, target):
    if node is None:
        return False

    if node is target:
        if node.left is None or node.right is None:
            print(f'Node found: {node}')
            result = delete_base_case(node)
        else:
            swap_node = bst_node.prev_element(node)
            print(f'Swap node: {swap_node}')
            bst_node.swap(node, swap_node)
            result = delete_node(node.left, target)
    elif node.key > target.key:
        result = delete_node(node.left, target)
    else:
        result = delete_node(node.right, target)

    update_attributes(node)
    balance(node)

    return result


def delete(node, key):
    if node is None:
        return False

    if node.key == key:
        if node.left is None or node.right is None:
            print(f'Node found: {node}')
            result = delete_base_case(node)
        else:
            swap_node = bst_node.prev_element(node)
            print(f'Swap node: {swap_node}')
            bst_node.swap(node, swap_node)
            result = delete_node(node.left, swap_node)
    elif node.key > key:
        result = delete(node.left, key)
    else:
        result = delete(node.right, key)

    update_attributes(node)
    balance(node)

    return result


def order_statistics(node, k):
    if node is None:
        return None
    left_size = get_size(node.left)
    if k == left_size + 1:
        return node
    if k < left_size + 1:
        return order_statistics(node.left, k)
    else:
        return order_statistics(node.right, k - left_size - 1)


def avl_merge_with_root(node1, node2, root):
    h1 = get_height(node1)
    h2 = get_height(node2)
    if abs(h1 - h2) <= 1:
        bst_node.merge_with_root(node1, node2, root)
        update_attributes(root)
        return root
    elif h1 > h2:
        new_root = avl_merge_with_root(node1.right, node2, root)
        node1.right = new_root
        new_root.parent = node1
        return balance(node1)
    else:
        new_root = avl_merge_with_root(node1, node2.left, root)
        node2.left = new_root
        new_root.parent = node2
        return balance(node2)


def avl_merge(node1, node2):
    if node1 is None and node2 is None:
        return None
    elif node1 is None:
        return node2
    elif node2 is None:
        return node1

    root = node1.maximum()
    delete_base_case(root)
    node1 = root.root()
    # удаление корня меняет его родителя, поэтому приводим в изначальное состояние
    bst_node.clear_parent(root)

    return avl_merge_with_root(node1, node2, root)


def avl_split(node, key):
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
        left, temp = avl_split(node.left, key)
        bst_node.clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        # Корень и всё его левое поддерево должны отправиться в 1 часть ответа,
        # потому что там всё меньше или равно key.
        # В правом же поддереве могут быть как ключи <= key, так и > key,
        # поэтому продолжаем резать.
        # После этого правая часть разреза сразу идёт как 2 часть ответа,
        # а чтобы получить первую, сливаем левые части.
        temp, right = avl_split(node.right, key)
        bst_node.clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)
    bst_node.clear_parent(left, right)
    return left, right


