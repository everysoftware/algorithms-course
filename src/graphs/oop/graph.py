from __future__ import annotations

from typing import TYPE_CHECKING, Generic, Self

from src.graphs.oop.models import Edge, EdgeData, K, Node, Weight
from src.graphs.oop.operations import (
    bfs,
    dfs,
    dfs_iterative,
    dijkstra,
    dijkstra_heap,
    find_path,
    find_path_all,
    find_shortest_path,
)

if TYPE_CHECKING:
    from collections.abc import Iterable


class Graph(Generic[K]):
    """
    ООП-представление графа.
    """

    nodes: dict[K, Node[K]]
    """
    Словарь узлов графа.
    """

    def __init__(self, nodes: dict[K, Node[K]] | None = None) -> None:
        self.nodes = nodes if nodes is not None else {}

    @staticmethod
    def edge_exists(node_from: Node[K], node_to: Node[K]) -> bool:
        """
        Проверяет, есть ли ребро между двумя узлами.
        """
        return node_to in node_from.parents

    @staticmethod
    def find_path(start: Node[K], end: Node[K]) -> list[K]:
        """
        Находит путь между двумя узлами.
        """
        return find_path(start, end)

    @staticmethod
    def find_path_all(start: Node[K], end: Node[K]) -> list[list[K]]:
        """
        Находит все пути между двумя узлами.
        """
        return find_path_all(start, end)

    @staticmethod
    def find_shortest_path(start: Node[K], end: Node[K]) -> list[K]:
        """
        Находит кратчайший путь между двумя узлами.
        """
        return find_shortest_path(start, end)

    @classmethod
    def from_edge_list(cls, edges: Iterable[EdgeData[K]]) -> Self:
        """
        Создает граф из списка ребер.
        """
        graph = cls()
        for key_from, key_to, weight in edges:
            node_from = graph.add(key_from) if not graph.contains(key_from) else graph.get(key_from)
            node_to = graph.add(key_to) if not graph.contains(key_to) else graph.get(key_to)
            graph.connect(node_from, node_to, weight)
        return graph

    def get(self, key: K) -> Node[K]:
        """
        Возвращает узел по его ключу.
        """
        return self.nodes[key]

    def contains(self, key: K) -> bool:
        """
        Проверяет, есть ли узел с таким ключом в графе.
        """
        return key in self.nodes

    def add(self, key: K) -> Node[K]:
        """
        Добавляет узел в граф.
        """
        if self.contains(key):
            raise ValueError(f"Node with value {key} already exists")

        node = Node(key)
        self.nodes[key] = node

        return node

    def connect(self, node_from: Node[K], node_to: Node[K], weight: Weight) -> Edge:
        """
        Добавляет ребро в граф.
        """
        if self.edge_exists(node_from, node_to):
            raise ValueError(f"Edge from {node_from.key} to {node_to.key} already exists")

        edge = Edge(node_to, weight)
        node_from.edges.append(edge)
        node_to.parents[node_from] = edge

        return edge

    def dfs(self, node: Node[K] | None = None, *, iterative: bool = True) -> list[K]:
        """
        Обход графа в глубину.
        """
        nodes = self.nodes.values() if node is None else {node}
        func = dfs_iterative if iterative else dfs
        return func(nodes)

    def bfs(self, node: Node[K] | None = None) -> list[K]:
        """
        Обход графа в ширину.
        """
        nodes = self.nodes.values() if node is None else {node}
        return bfs(nodes)

    def dijkstra(self, start: Node[K], end: Node[K], *, use_heap: bool = True) -> list[K]:
        """
        Алгоритм Дейкстры.
        """
        func = dijkstra_heap if use_heap else dijkstra
        return func(self.nodes.values(), start, end)
