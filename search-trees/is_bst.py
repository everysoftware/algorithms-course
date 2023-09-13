from bst_node import BSTNode
from traversal import dfs_inorder_iter


def is_bst_naive(a, root):
    return dfs_inorder_iter(root) == sorted(x[0] for x in a)


def is_bst(root, min_key=float('-inf'), max_key=float('inf')):
    if root is None:
        return True
    if root.key < min_key or root.key > max_key:
        return False
    return is_bst(root.left, min_key, root.key) and\
        is_bst(root.right, root.key, max_key)


def is_bst_inorder(root, prev=BSTNode(float('-inf'))):
    if root is None:
        return True
    # Проверяем левое поддерево.
    left = is_bst_inorder(root.left, prev)
    # Значение текущего узла должно быть больше предыдущего.
    if root.key <= prev.key:
        return False
    # Обновляем данные предыдущего узла и проверяем правое поддерево.
    prev.key = root.key
    return left and is_bst_inorder(root.right, prev)


def is_bst_iter(root):
    st = []
    prev = BSTNode(float('-inf'))
    node = root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            if prev.key > node.key:
                return False
            prev = node
            node = node.right
    return True


def is_general_bst(root):
    st = []
    prev = BSTNode(float('-inf'))
    node = root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            if prev.key > node.key or prev.key == node.key and node.left is prev:
                return False
            prev = node
            node = node.right
    return True
