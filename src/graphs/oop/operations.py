import heapq
from collections import deque
from collections.abc import Iterable

from src.graphs.oop.models import K, Node, PathNode


def dfs(nodes: Iterable[Node[K]]) -> list[K]:
    """
    Обход графа в глубину.
    """
    visited: set[K] = set()
    result: list[K] = []

    # Одного прохода может быть недостаточно для обхода всего графа, если он несвязный
    for node in nodes:
        if node.key not in visited:
            _dfs(node, visited, result)

    return result


def dfs_iterative(nodes: Iterable[Node[K]]) -> list[K]:
    """
    Обход графа в глубину.
    """
    visited: set[K] = set()
    result: list[K] = []

    for node in nodes:
        if node.key not in visited:
            _dfs_iterative(node, visited, result)

    return result


def bfs(nodes: Iterable[Node[K]]) -> list[K]:
    """
    Обход графа в ширину.
    """
    visited: set[K] = set()
    result: list[K] = []

    for node in nodes:
        if node.key not in visited:
            _bfs(node, visited, result)

    return result


def dijkstra(nodes: Iterable[Node[K]], start: Node[K], end: Node[K]) -> list[K]:
    """
    Алгоритм Дейкстры.

    Сложность алгоритма: O(V^2 + E)
    """
    nodes_set = set(nodes)
    unprocessed: set[Node[K]] = nodes_set.copy()
    time = {node: float("inf") for node in nodes_set}
    time[start] = 0
    previous = {}

    while unprocessed:
        # O(V) для каждой вершины = O(V^2)
        current_node = min(unprocessed, key=lambda node: time[node])

        if time[current_node] == float("inf"):
            break

        unprocessed.remove(current_node)

        # O(1) для каждого ребра = O(E)
        for edge in current_node.edges:
            if edge.adjacent in unprocessed:
                new_time = time[current_node] + edge.weight

                if new_time < time[edge.adjacent]:
                    time[edge.adjacent] = new_time
                    previous[edge.adjacent] = current_node

    if time[end] == float("inf"):
        return []

    return _dijkstra_extract_path(previous, start, end)


def dijkstra_heap(nodes: Iterable[Node[K]], start: Node[K], end: Node[K]) -> list[K]:
    """
    Алгоритм Дейкстры на куче.

    Сложность алгоритма: O((V + E) * log(V))
    """
    time = {node: float("inf") for node in nodes}
    time[start] = 0
    previous = {}
    queue: list[tuple[float, Node[K]]] = [(0, start)]

    while queue:
        # O(logN) для каждой вершины = O(V * log(V))
        current_time, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_time > time[current_node]:
            continue

        # O(logN) для каждого ребра = O(E * log(V))
        for edge in current_node.edges:
            new_time = current_time + edge.weight
            if new_time < time[edge.adjacent]:
                time[edge.adjacent] = new_time
                previous[edge.adjacent] = current_node
                heapq.heappush(queue, (new_time, edge.adjacent))

    if time[end] == float("inf"):
        return []

    return _dijkstra_extract_path(previous, start, end)


def find_path(
    start: Node[K],
    end: Node[K],
    visited: set[K] | None = None,
    path: list[K] | None = None,
) -> list[K]:
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(start.key)
    visited.add(start.key)

    if start == end:
        return path

    for edge in start.edges:
        if edge.adjacent.key not in visited and find_path(edge.adjacent, end, visited, path):
            return path

    return []


def find_path_all(
    start: Node[K],
    end: Node[K],
    visited: set[K] | None = None,
    path: list[K] | None = None,
    paths: list[list[K]] | None = None,
) -> list[list[K]]:
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if paths is None:
        paths = []

    path.append(start.key)
    visited.add(start.key)

    if start == end:
        paths.append(path.copy())

    for edge in start.edges:
        if edge.adjacent.key not in visited:
            find_path_all(edge.adjacent, end, visited, path, paths)

    visited.remove(start.key)
    path.pop()

    return paths


def find_shortest_path(start: Node[K], end: Node[K], visited: set[K] | None = None) -> list[K]:
    if visited is None:
        visited = set()

    queue = deque([PathNode(start, None)])

    while queue:
        path_node = queue.popleft()
        visited.add(path_node.node.key)

        # Если найден конечный узел, то возвращаем путь.
        if path_node.node == end:
            return _shortest_path_extract_path(path_node)

        for edge in path_node.node.edges:
            if edge.adjacent.key not in visited:
                # Оптимизация: если смежный узел является конечным, то кладем его в начало очереди.
                if edge.adjacent == end:
                    queue.appendleft(PathNode(edge.adjacent, path_node))
                    continue

                visited.add(edge.adjacent.key)
                queue.append(PathNode(edge.adjacent, path_node))

    return []


def _dfs(node: Node[K], visited: set[K] | None = None, result: list[K] | None = None) -> list[K]:
    """
    Обход графа в глубину (только связные графы).
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    # Посещение вершин даёт сложность O(V)
    visited.add(node.key)
    result.append(node.key)

    # Цикл перебора рёбер даёт сложность O(E)
    for edge in node.edges:
        if edge.adjacent.key not in visited:
            _dfs(edge.adjacent, visited, result)

    return result


def _dfs_iterative(node: Node[K], visited: set[K] | None = None, result: list[K] | None = None) -> list[K]:
    """
    Итеративный обход графа в глубину (толкько связные графы)
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node.key)
            result.append(node.key)
            for edge in node.edges:
                if edge.adjacent.key not in visited:
                    stack.append(edge.adjacent)  # noqa: PERF401

    return result


def _bfs(node: Node[K], visited: set[K] | None = None, result: list[K] | None = None) -> list[K]:
    """
    Обход графа в ширину (только связные графы).
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    queue = deque([node])

    while queue:
        node = queue.popleft()
        visited.add(node.key)
        result.append(node.key)

        for edge in node.edges:
            if edge.adjacent.key not in visited:
                visited.add(edge.adjacent.key)
                queue.append(edge.adjacent)

    return result


def _dijkstra_extract_path(previous: dict[Node[K], Node[K]], start: Node[K], end: Node[K]) -> list[K]:
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node.key)
        current_node = previous[current_node]

    path.append(start.key)
    return path[::-1]


def _shortest_path_extract_path(path_node: PathNode | None) -> list[K]:
    """
    Извлечение пути.
    """
    path = []
    while path_node:
        path.append(path_node.node.key)
        path_node = path_node.parent
    return path[::-1]
