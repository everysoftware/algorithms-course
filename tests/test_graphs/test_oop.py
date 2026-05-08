import pytest

from src.graphs.oop.graph import Graph
from tests.test_graphs.mocks import graphs


@pytest.mark.parametrize(
    ("graph", "expected"),
    [
        (graphs["short"], [1, 2, 3]),
        (graphs["long"], [1, 2, 5, 4, 3, 7]),
    ],
)
def test_dfs(graph: Graph[int], expected: list[int]) -> None:
    result = graph.dfs(iterative=False)
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "expected"),
    [
        (graphs["short"], [1, 3, 2]),
        (
            graphs["long"],
            [1, 2, 5, 4, 3, 7],
        ),
    ],
)
def test_dfs_iterative(graph: Graph[int], expected: list[int]) -> None:
    result = graph.dfs(iterative=True)
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "expected"),
    [
        (graphs["short"], [1, 2, 3]),
        (
            graphs["long"],
            [1, 2, 5, 4, 3, 7],
        ),
    ],
)
def test_bfs(graph: Graph[int], expected: list[int]) -> None:
    result = graph.bfs()
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "start", "end", "expected"),
    [
        (graphs["short"], 1, 3, [1, 2, 3]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_path(graph: Graph[int], start: int, end: int, expected: list[int]) -> None:
    result = graph.find_path(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "start", "end", "expected"),
    [
        (graphs["short"], 1, 3, [[1, 2, 3], [1, 3]]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_path_all(graph: Graph[int], start: int, end: int, expected: list[list[int]]) -> None:
    result = graph.find_path_all(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "start", "end", "expected"),
    [
        (graphs["short"], 1, 3, [1, 3]),
        (graphs["short"], 2, 1, []),
    ],
)
def test_find_shortest_path(graph: Graph[int], start: int, end: int, expected: list[int]) -> None:
    result = graph.find_shortest_path(graph.get(start), graph.get(end))
    assert result == expected


@pytest.mark.parametrize(
    ("graph", "start", "end", "expected"),
    [
        (graphs["short"], 1, 3, [1, 2, 3]),
        (graphs["short"], 2, 1, []),
        (graphs["long2"], 1, 6, [1, 3, 5, 6]),
    ],
)
def test_dijkstra(graph: Graph[int], start: int, end: int, expected: list[int]) -> None:
    result = graph.dijkstra(graph.get(start), graph.get(end), use_heap=False)
    assert result == expected

    result_heap = graph.dijkstra(graph.get(start), graph.get(end), use_heap=True)
    assert result_heap == expected
