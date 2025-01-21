import pytest

from src.a_intro.summary_ranges import summary_ranges


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ["0->9"]),
    ],
)
def test_summary_ranges(nums: list[int], expected: list[str]) -> None:
    assert summary_ranges(nums) == expected
