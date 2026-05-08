from dataclasses import dataclass

K = int
Weight = float
EdgeData = tuple[K, K, Weight]

# Representations
EdgeList = list[EdgeData]
AdjacencyMatrix = list[list[Weight]]
AdjacencyList = dict[K, list[tuple[K, Weight]]]


@dataclass
class GraphData:
    """
    Данные о графе для его создания.
    """

    size: int
    edges: EdgeList


def edge_list(graph: GraphData) -> EdgeList:
    """
    Возвращает список ребер графа.
    """
    return graph.edges


def adjacency_matrix(graph: GraphData) -> AdjacencyMatrix:
    """
    Возвращает матрицу смежности графа.
    """
    matrix = [[0.0 for _ in range(graph.size)] for _ in range(graph.size)]

    for edge in graph.edges:
        matrix[edge[0] - 1][edge[1] - 1] = edge[2]

    return matrix


def adjacency_list(graph: GraphData) -> AdjacencyList:
    """
    Возвращает список смежности графа.
    """
    lst: AdjacencyList = {}

    for edge in graph.edges:
        if edge[0] not in lst:
            lst[edge[0]] = []
        lst[edge[0]].append((edge[1], edge[2]))

    return lst
