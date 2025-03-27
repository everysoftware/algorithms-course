import pytest

from src.g_prefix_sums.product_except_self import product_except_self


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_product_except_self(nums: list[int], expected: list[int]) -> None:
    assert product_except_self(nums) == expected
