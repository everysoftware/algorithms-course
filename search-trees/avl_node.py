from bst_node import BSTNode, prev_element, merge_with_root, clear_parent


class AVLNode(BSTNode):
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        super().__init__(key, value, parent, left, right)
        self.height = 0
        self.size = 1

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'{type(self).__name__}(K: {self.key}, V: {self.value} H: {self.height}, S: {self.size}, P: {parent}, ' \
               f'L: {left}, R: {right})'

    def __repr__(self):
        return super().__repr__()

    def insert(self, key, value=None):
        return avl_insert(self, key, value)

    def delete(self, key):
        return avl_delete(self, key)

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

    def update_attributes(self):
        update_size(self)
        update_height(self)


def get_height(node):
    return node.height if node is not None else -1


def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1


def update_height_recursive(node):
    if node is None:
        return -1
    node.height = max(update_height_recursive(node.left), update_height_recursive(node.right)) + 1
    return node.height


def get_size(node):
    return node.size if node is not None else 0


def update_size(node):
    node.size = get_size(node.left) + get_size(node.right) + 1


def update_size_recursive(node):
    if node is None:
        return 0
    node.size = update_size_recursive(node.left) + update_size_recursive(node.right) + 1
    return node.size


def update_attributes(node):
    if node is None:
        return
    node.update_attributes()


# Коэффициент сбалансированности:
# если get_balance(x) <= 1, то всё хорошо.
# если get_balance(x) = -2, значит, слева высота больше, поэтому балансируем дерево вправо.
# если get_balance(x) = 2, значит, больше высота справа, и нужно балансировать дерево влево.
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)


def check_height(node):
    if not isinstance(node, AVLNode):
        return True
    return all(get_height(x) == max(get_height(x.left), get_height(x.right)) + 1 for x in node.in_order())


def check_size(node):
    if not isinstance(node, AVLNode):
        return True
    return all(get_size(x) == get_size(x.left) + get_size(x.right) + 1 for x in node.in_order())


def check_balance(node):
    if not isinstance(node, AVLNode):
        return True
    return all(abs(get_balance(x)) <= 1 for x in node.in_order())


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
    if node is None:
        return
    update_attributes(node)
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


def avl_insert(node, key, value, parent=None):
    if node is None and isinstance(parent, AVLNode):
        return type(parent)(key, value, parent)
    elif node is None and not isinstance(parent, AVLNode):
        return None
    if node.key > key:
        node.left = avl_insert(node.left, key, value, node)
    elif node.key < key:
        node.right = avl_insert(node.right, key, value, node)
    return balance(node)


def avl_delete(node, key):
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
            node.left = avl_delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = avl_delete(node.left, key)
    else:
        node.right = avl_delete(node.right, key)
    return balance(node)


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


def avl_merge_with_root(left, right, root):
    if root is None:
        return None
    h1 = get_height(left)
    h2 = get_height(right)
    if abs(h1 - h2) <= 1:
        merge_with_root(left, right, root)
        update_attributes(root)
        return balance(root)
    elif h1 > h2:
        new_root = avl_merge_with_root(left.right, right, root)
        left.right = new_root
        new_root.parent = left
        update_attributes(left)
        return balance(left)
    else:
        new_root = avl_merge_with_root(left, right.left, root)
        right.left = new_root
        new_root.parent = right
        update_attributes(right)
        return balance(right)


def avl_merge(left, right):
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left
    new_root = left.maximum()
    left = avl_delete(left, new_root.key)
    clear_parent(new_root)
    return avl_merge_with_root(left, right, new_root)


def avl_split(node, key):
    if node is None:
        return None, None
    if node.key > key:
        left, temp = avl_split(node.left, key)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = avl_split(node.right, key)
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)
    clear_parent(left, right)
    return left, right
