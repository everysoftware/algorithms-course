import pytest

from src.dnc.kth_largest import quick_select


@pytest.mark.parametrize(
    "a, k",
    [
        ([1, 2, 3, 4, 5], 3),
        ([5, 4, 3, 2, 1], 3),
        ([4, 5, 3, 2, 1], 3),
        ([1, 2, 3, 5, 4], 3),
        ([1, 1, 1, 1, 1], 2),
        ([1], 1),
    ],
)
def test_quick_select(a: list[int], k: int) -> None:
    assert quick_select(a, k) == sorted(a)[k - 1]
