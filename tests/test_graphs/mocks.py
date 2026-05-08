from src.graphs.oop.graph import Graph
from src.graphs.representations import GraphData

graph_data = {
    "short": GraphData(
        size=3,
        edges=[
            (1, 2, 3),
            (1, 3, 11),
            (2, 3, 7),
        ],
    ),
    "long": GraphData(
        size=7,
        edges=[
            (1, 2, 7),
            (2, 5, 3),
            (3, 2, 4),
            (4, 4, 0),
            (5, 4, 1),
            (7, 1, 5),
        ],
    ),
    "long2": GraphData(
        size=6,
        edges=[
            (1, 2, 7),
            (1, 3, 3),
            (3, 2, 8),
            (2, 4, 10),
            (4, 5, 3),
            (3, 5, 12),
            (4, 6, 7),
            (5, 6, 1),
        ],
    ),
}

graphs = {label: Graph.from_edge_list(data.edges) for label, data in graph_data.items()}
