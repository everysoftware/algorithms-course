"""
https://stepik.org/lesson/41234/step/2?unit=19818

Деревья имеют огромное количество применений в Computer Science. Они используются как для представления данных,
так и во многих алгоритмах машинного обучения. Далее мы также узнаем, как сбалансированные деревья используются
для реализации словарей. Данные структуры данных так или иначе используются во всех языках программирования и
базах данных. Ваша цель в данной задаче — научиться хранить и эффективно обрабатывать деревья, даже если в них
сотни тысяч вершин.

Формат входа. Первая строка содержит натуральное число n. Вторая строка содержит n целых чисел
parent[0], ... , parent[n − 1]. Для каждого 0 ≤ i ≤ n−1, parent[i] — родитель вершины i; если parent[i] = −1,
то i является корнем. Гарантируется, что корень ровно один. Гарантируется, что данная последовательность задаёт
дерево.

Формат выхода. Высота дерева.
"""


def tree_height_naive(a: list[int], parent: int = -1) -> int:
    """Наивное решение. Рекурсивно обходим все вершины дерева и находим высоту. Сложность O(N^2)."""
    height = 0

    # Находим всех детей вершины parent.
    children = [i for i, j in enumerate(a) if j == parent]

    for child in children:
        height = max(height, 1 + tree_height_naive(a, child))

    return height


def build_tree(a: list[int]) -> tuple[int, list[list[int]]]:
    """Построение дерева. Сложность O(N)."""
    n = len(a)
    root = -1
    adjacency_list: list[list[int]] = [[] for _ in range(n)]

    for i in range(n):
        if a[i] == -1:
            root = i
        else:
            adjacency_list[a[i]].append(i)

    return root, adjacency_list


def dfs_iterative(root: int, adjacency_list: list[list[int]]) -> int:
    """Обход дерева в глубину. Сложность O(N)"""
    n = len(adjacency_list)
    height = [1] * n
    """height[i] - высота дерева заканчивающегося в i-й вершине"""
    stack = [root]
    visited = [False] * n

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True

            for child in adjacency_list[node]:
                stack.append(child)
                height[child] += height[node]

    return max(height)


def tree_height_stack(a: list[int]) -> int:
    """Решение с использованием стека. Сложность O(N)."""
    root, adjacency_list = build_tree(a)
    return dfs_iterative(root, adjacency_list)
