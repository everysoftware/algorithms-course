from collections import deque


# O(n^2)
def tree_height_naive(parents: list[int], node: int = -1) -> int:
    n = len(parents)
    height = 0
    # Находим детей текущего узла
    children = [i for i in range(n) if parents[i] == node]
    for child in children:
        height = max(height, 1 + tree_height_naive(parents, child))
    return height


# O(n)
def tree_height_dfs(parents: list[int]) -> int:
    root, adjacency_list = build_tree(parents)
    return dfs_iterative(root, adjacency_list)


# O(n)
def build_tree(parents: list[int]) -> tuple[int, list[list[int]]]:
    n = len(parents)
    root = -1
    # Создаем список смежности
    tree: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    return root, tree


# O(n)
def dfs_iterative(node: int, tree: list[list[int]]) -> int:
    n = len(tree)
    # dp[i] - высота дерева заканчивающегося в i-й вершине
    dp = [1] * n
    stack = [node]
    visited = [False] * n
    while stack:
        curr = stack.pop()
        if visited[curr]:
            continue
        visited[curr] = True
        for child in tree[curr]:
            stack.append(child)
            # Обновляем высоту дерева для текущего узла
            dp[child] = max(dp[child], dp[curr] + 1)
    return max(dp)


# O(n)
def tree_height_bfs(parents: list[int]) -> int:
    root, adjacency_list = build_tree(parents)
    return bfs(root, adjacency_list)


# O(n)
def bfs(node: int, tree: list[list[int]]) -> int:
    n = len(tree)
    dp = [1] * n
    queue = deque([node])
    visited = [False] * n
    while queue:
        curr = queue.popleft()
        if visited[curr]:
            continue
        visited[curr] = True
        for child in tree[curr]:
            queue.append(child)
            dp[child] = max(dp[child], dp[curr] + 1)
    return max(dp)
