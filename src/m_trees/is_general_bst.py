from src.m_trees.dfs import BNode, build_tree
from src.m_trees.dfs_iterative import dfs_iterative

INF = 10**20


# O(n log n)
def is_general_bst_fake(nodes: list[tuple[int, int, int]]) -> bool:
    if not nodes:
        return True
    expected_keys = sorted(x[0] for x in nodes)
    root = build_tree(nodes)
    actual_keys = dfs_iterative(root)
    return actual_keys == expected_keys


# O(n)
def is_general_bst_dfs(nodes: list[tuple[int, int, int]]) -> bool:
    if not nodes:
        return True
    node = build_tree(nodes)
    st: list[tuple[BNode | None, int, int]] = [(node, -INF, INF)]
    while st:
        curr, min_key, max_key = st.pop()
        if curr is None:
            continue
        # Проверяем, что ключ текущего узла находится в допустимом диапазоне.
        if curr.key < min_key or curr.key > max_key:
            return False
        # Добавляем правое и левое поддерево в стек.
        st.append((curr.right, curr.key, max_key))
        st.append((curr.left, min_key, curr.key - 1))
    return True
