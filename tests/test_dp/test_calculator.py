import pytest

from dp import calculator


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [1]),
        (5, [1, 2, 4, 5]),
        (10, [1, 3, 9, 10]),
        (
            74074,
            [
                1,
                2,
                6,
                18,
                19,
                57,
                171,
                513,
                514,
                1542,
                1543,
                3086,
                9258,
                9259,
                18518,
                37036,
                37037,
                74074,
            ],
        ),
        (
            96234,
            [
                1,
                3,
                9,
                10,
                11,
                22,
                66,
                198,
                594,
                1782,
                5346,
                16038,
                16039,
                32078,
                96234,
            ],
        ),
    ],
)
def test_calculator(n: int, expected: list[int]):
    assert calculator(n) == expected
