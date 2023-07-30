"""
Задача 1. https://stepik.org/lesson/45970/step/1
Реализовать обходы дерева.

Обход дерева в стиле DFS Preorder: Node -> Left -> Right
Обход дерева в стиле DFS Inorder: Left -> Node -> Right
Обход дерева в стиле DFS Postorder: Left -> Right -> Node

Сложность: O(N)
"""


def dfs_preorder(root):
    if root is None:
        return []
    return [root.key] + dfs_preorder(root.left) + dfs_preorder(root.right)


def dfs_inorder(root):
    if root is None:
        return []
    return dfs_inorder(root.left) + [root.key] + dfs_inorder(root.right)


def dfs_postorder(root):
    if root is None:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.key]


def traversal(a):
    return (dfs_inorder(a),
            dfs_preorder(a),
            dfs_postorder(a))


# Итеративные версии обходов


def dfs_preorder_iter(root):
    st = [root]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)
    return result


def dfs_inorder_iter(root):
    st = []
    result = []
    node = root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result.append(node.key)
            node = node.right
    return result


def dfs_postorder_iter(root):
    st = [root]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)
    result.reverse()
    return result


def traversal_iter(root):
    return (dfs_inorder_iter(root),
            dfs_preorder_iter(root),
            dfs_postorder_iter(root))
