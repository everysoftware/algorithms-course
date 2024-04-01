import pytest

from dp2 import max_score


@pytest.mark.parametrize(
    "budget, strength, gold, monster, expected",
    [
        (10, [1, 2, 3], [1, 2, 3], [1, 2, 3], 3),  # Обычный случай
        (0, [1, 2, 3], [1, 2, 3], [1, 2, 3], 0),  # Бюджет равен нулю
        (10, [], [], [], 0),  # Нет карт
        (10, [1, 2, 3], [1, 2, 3], [], 0),  # Нет монстров
        (
            10,
            [10, 20, 30],
            [1, 2, 3],
            [15, 25, 100],
            2,
        ),  # Некоторые монстры слишком сильные
        (
            10,
            [10, 20, 30],
            [1, 2, 3],
            [60],
            0,
        ),  # Равенство сил монстра и манчкина
    ],
)
def test_max_score(
    budget: int,
    strength: list[int],
    gold: list[int],
    monster: list[int],
    expected: int,
):
    assert max_score(budget, strength, gold, monster) == expected
