from typing import Literal

from src.m_trees.dfs import BNode, build_tree


# O(n)
def dfs_all_iterative(nodes: list[tuple[int, int, int]]) -> tuple[list[int], list[int], list[int]]:
    """
    Итеративный обход дерева в глубину (DFS). Возвращает три списка:
    - inorder (симметричный) обход
    - preorder (прямой) обход
    - postorder (обратный) обход
    """
    root = build_tree(nodes)
    return (
        dfs_iterative(root, "inorder"),
        dfs_iterative(root, "preorder"),
        dfs_iterative(root, "postorder"),
    )


# O(n)
def dfs_iterative(root: BNode, style: Literal["inorder", "preorder", "postorder"] = "inorder") -> list[int]:
    """
    Итеративный обход дерева в глубину (DFS).
    """
    match style:
        case "inorder":
            return dfs_inorder_iterative(root)
        case "preorder":
            return dfs_preorder_iterative(root)
        case "postorder":
            return dfs_postorder_iterative(root)
        case _:
            raise ValueError(f"Unknown DFS style: {style}")


# O(n)
def dfs_preorder_iterative(node: BNode) -> list[int]:
    """
    Итеративный обход дерева в глубину (DFS) в прямом порядке.
    """
    st = [node]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        # Кладем в стек правого потомка перед левого, чтобы левый обрабатывался первым
        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)
    return result


# O(n)
def dfs_postorder_iterative(node: BNode) -> list[int]:
    """
    Итеративный обход дерева в глубину (DFS) в обратном порядке.
    """
    st = [node]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        # Кладем в стек левого потомка перед правого, чтобы правый обрабатывался первым
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)
    # Поскольку мы добавляли узлы в обратном порядке, нужно развернуть результат
    result.reverse()
    return result


# O(n)
def dfs_inorder_iterative(node: BNode) -> list[int]:
    """
    Итеративный обход дерева в глубину (DFS) в симметричном порядке.
    """
    st: list[BNode] = []
    result: list[int] = []
    curr: BNode | None = node
    while st or curr is not None:
        # Переходим к самому левому узлу
        if curr is not None:
            st.append(curr)
            curr = curr.left
        else:
            # Когда достигли самого левого узла, обрабатываем егои переходим к правому
            curr = st.pop()
            result.append(curr.key)
            curr = curr.right
    return result
