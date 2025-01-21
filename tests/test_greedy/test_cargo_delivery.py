import pytest

from src.greedy.knapsack import greedy_knapsack


@pytest.mark.parametrize(
    "w, items, expected",
    [
        (50, [(60, 20), (100, 50), (120, 30)], 180.000),  # Основной сценарий
        (
            0,
            [(60, 20), (100, 50), (120, 30)],
            0.000,
        ),  # Вместимость рюкзака равна нулю
        (50, [(60, 20)], 60.000),  # Только один предмет
        (50, [], 0.000),  # Нет предметов
        (
            10,
            [(60, 20), (100, 50), (120, 30)],
            40.000,
        ),  # Вместимость рюкзака меньше веса любого предмета
        (
            100,
            [(60, 20), (100, 50), (120, 30)],
            280.000,
        ),  # Вместимость рюкзака больше суммарного веса всех предметов
    ],
)
def test_cargo_delivery(w: int, items: list[tuple[int, int]], expected: float) -> None:
    assert round(greedy_knapsack(w, items), 3) == expected
