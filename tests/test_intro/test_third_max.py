import pytest

from src.intro.third_max import third_max


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 1], 1),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 2, 3, 3, 4, 4, 5, 5], 3),
    ],
)
def test_third_max(nums: list[int], expected: int) -> None:
    assert third_max(nums) == expected
