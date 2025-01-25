# O(n^2)
def tree_height_naive(a: list[int], parent: int = -1) -> int:
    height = 0
    # Находим всех детей вершины parent.
    children = [i for i, j in enumerate(a) if j == parent]
    for child in children:
        height = max(height, 1 + tree_height_naive(a, child))
    return height


# O(n)
def tree_height_stack(a: list[int]) -> int:
    root, adjacency_list = build_tree(a)
    return dfs_iterative(root, adjacency_list)


# O(n)
def build_tree(a: list[int]) -> tuple[int, list[list[int]]]:
    n = len(a)
    root = -1
    adjacency_list: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        if a[i] == -1:
            root = i
        else:
            adjacency_list[a[i]].append(i)
    return root, adjacency_list


# O(n)
def dfs_iterative(root: int, adjacency_list: list[list[int]]) -> int:
    n = len(adjacency_list)
    # height[i] - высота дерева заканчивающегося в i-й вершине
    dp = [1] * n
    stack = [root]
    visited = [False] * n
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for child in adjacency_list[node]:
                stack.append(child)
                dp[child] += dp[node]
    return max(dp)
