import pytest

from src.d_sorting.partition import partition2, partition3


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 4),
        ([4, 5, 3, 2, 1], 3),
        ([1, 2, 3, 5, 4], 0),
        ([1, 1, 1, 1, 1], 4),
        ([1], 0),
    ],
)
def test_partition2(a: list[int], expected: int) -> None:
    assert partition2(a) == expected


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        ([1, 2, 3, 4, 5], (0, 0)),
        ([5, 4, 3, 2, 1], (4, 4)),
        ([4, 5, 3, 2, 1], (3, 3)),
        ([1, 2, 3, 5, 4], (0, 0)),
        ([1, 1, 1, 1, 1], (0, 4)),
        ([1], (0, 0)),
    ],
)
def test_partition3(a: list[int], expected: tuple[int, int]) -> None:
    assert partition3(a) == expected
