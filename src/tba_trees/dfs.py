def dfs_wrapper(tree: dict[str, list[str]], node: str, visited: set[str], result: list[str]) -> list[str]:
    # посещение вершины
    visited.add(node)
    result.append(node)

    # переход к детям этой вершины
    for child in tree[node]:
        if child not in visited:
            dfs_wrapper(tree, child, visited, result)

    return result


def dfs(tree: dict[str, list[str]], node: str) -> list[str]:
    return dfs_wrapper(tree, node, set(), [])


def dfs_iterative(tree: dict[str, list[str]], start: str) -> list[str]:
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            # посещаем вершину
            visited.add(node)
            result.append(node)
            # добавляем детей в стек
            stack.extend(tree[node])
    return result
