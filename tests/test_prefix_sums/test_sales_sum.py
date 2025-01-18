import pytest

from src.prefix_sums.sales_sum import sales_sum


@pytest.mark.parametrize(
    "sales, queries, expected",
    [
        # Тест 1: Проверка на примере
        (
            [100, 200, 300, 400, 500],
            [(1, 3), (2, 4), (1, 5)],
            [600, 900, 1500],
        ),
        # Тест 2: Проверка на массиве с одним элементом
        ([100], [(1, 1)], [100]),
        # Тест 3: Проверка на массиве с двумя элементами
        ([100, 200], [(1, 2)], [300]),
        ([100, 200], [(1, 1), (2, 2)], [100, 200]),
        # Тест 4: Проверка на массиве с несколькими элементами
        ([100, 200, 300, 400, 500], [(1, 5)], [1500]),
        (
            [100, 200, 300, 400, 500],
            [(1, 3), (2, 4), (3, 5)],
            [600, 900, 1200],
        ),
    ],
)
def test_sales_sum(sales: list[int], queries: list[tuple[int, int]], expected: list[int]):
    assert sales_sum(sales, queries) == expected
