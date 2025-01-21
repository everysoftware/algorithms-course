import pytest

from src.e_two_pointers.water import max_area


@pytest.mark.parametrize("height, expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)])
def test_max_area(height: list[int], expected: int) -> None:
    assert max_area(height) == expected
