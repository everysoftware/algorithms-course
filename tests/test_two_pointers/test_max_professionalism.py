import pytest

from two_pointers import max_professionalism


@pytest.mark.parametrize(
    "a, expected",
    [([1, 3, 5, 7, 9], 21), ([1, 2, 3, 4, 5], 14), ([1, 1, 1, 1, 1], 5)],
)
def test_max_professionalism(a: list[int], expected: int):
    assert max_professionalism(a) == expected
