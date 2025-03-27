from collections.abc import Callable

import pytest

from src.k_dp.gold_storage_robbery import rob_gold_storage_dp, rob_gold_storage_dp2


@pytest.mark.parametrize(
    "func",
    [rob_gold_storage_dp2, rob_gold_storage_dp],
)
@pytest.mark.parametrize(
    "w, weight, expected",
    [
        (
            10,
            [1, 4, 8],
            9,
        ),  # рюкзак может вместить все предметы, но не все вместятся
        (10, [1, 2, 3, 4, 5], 10),  # рюкзак может вместить все предметы
        (
            5,
            [4, 5, 1],
            5,
        ),  # рюкзак может вместить один тяжелый предмет или несколько легких
        (0, [1, 2, 3], 0),  # рюкзак не может вместить ничего
        (5, [], 0),  # нет предметов для помещения в рюкзак
        (139, [2, 3, 4, 8, 10, 20, 100], 139),
        (10, [100], 0),
    ],
)
def test_gold_storage(
    func: Callable[[int, list[int]], int],
    w: int,
    weight: list[int],
    expected: int,
) -> None:
    assert func(w, weight) == expected
