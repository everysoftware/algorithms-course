import pytest

from src.h_dp.coin_change import coin_change


@pytest.mark.parametrize(
    ("coins", "n", "expected"),
    [
        ([1, 3, 5, 10], 1, 1),
        ([1, 3, 5, 10], 2, 2),
        ([1, 3, 5, 10], 3, 1),
        ([1, 3, 5, 10], 4, 2),
        ([1, 3, 5, 10], 5, 1),
        ([1, 3, 5, 10], 6, 2),
        ([1, 3, 5, 10], 7, 3),
        ([1, 3, 5, 10], 8, 2),
        ([1, 3, 5, 10], 9, 3),
        ([1, 3, 5, 10], 0, 0),
        ([1, 3, 5, 10], 4242, 426),
    ],
)
def test_coin_change(coins: list[int], n: int, expected: int) -> None:
    assert coin_change(coins, n) == expected
