from typing import Callable

import pytest

from greedy import act_sel, act_sel_other_approach


@pytest.mark.parametrize("func", [act_sel, act_sel_other_approach])
@pytest.mark.parametrize(
    "acts, expected",
    [
        (
            [
                (50, 66),
                (53, 78),
                (51, 61),
                (14, 32),
                (81, 93),
                (48, 95),
                (2, 57),
                (43, 80),
                (25, 55),
                (95, 98),
                (99, 100),
                (91, 93),
                (37, 62),
                (77, 83),
                (54, 66),
                (61, 79),
                (89, 93),
                (74, 99),
                (35, 48),
                (74, 87),
                (97, 98),
                (90, 97),
                (65, 91),
                (35, 49),
                (49, 56),
                (22, 98),
                (34, 56),
                (71, 74),
                (45, 94),
                (97, 99),
                (16, 68),
                (9, 36),
                (37, 52),
                (60, 100),
                (85, 92),
                (25, 87),
                (83, 90),
                (17, 48),
                (47, 64),
                (37, 67),
            ],
            [
                (14, 32),
                (35, 48),
                (49, 56),
                (71, 74),
                (77, 83),
                (83, 90),
                (91, 93),
                (95, 98),
                (99, 100),
            ],
        )
    ],
)
def test_act_sel(
    func: Callable[[list[tuple[int, int]]], list[tuple[int, int]]],
    acts: list[tuple[int, int]],
    expected: list[tuple[int, int]],
):
    assert func(acts) == expected
