import pytest

from src.base_ds import net_packets


@pytest.mark.parametrize(
    "size, packets, expected",
    [
        (1, [], []),
        (1, [(0, 0)], [0]),
        (1, [(0, 1), (0, 1)], [0, -1]),
        (1, [(0, 1), (1, 1)], [0, 1]),
        (
            2,
            [(0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (1, 1), (1, 2), (1, 3)],
            [0, 0, 0, 1, 1, 1, 2, -1],
        ),
        (
            2,
            [(0, 0), (0, 0), (0, 0), (1, 1), (1, 0), (1, 0), (1, 2), (1, 3)],
            [0, 0, 0, 1, 2, -1, -1, -1],
        ),
        (5, [(9, 1), (10, 0), (10, 1), (10, 0), (10, 0)], [9, 10, 10, 11, 11]),
    ],
)
def test_net_packets(
    size: int, packets: list[tuple[int, int]], expected: list[int]
):
    assert net_packets(size, packets) == expected
