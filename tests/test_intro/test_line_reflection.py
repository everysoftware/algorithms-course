import pytest

from src.a_intro.line_reflection import is_reflected


@pytest.mark.parametrize(
    ("points", "expected"),
    [
        ([[1, 1], [-1, 1]], True),
        ([[1, 1], [-1, -1]], False),
        ([[0, 0], [1, 0], [3, 0]], False),
        ([[1, 1], [1, 1], [1, 1]], True),
        ([[1, 1], [1, 1], [1, 1], [1, 1]], True),
        ([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], True),
        ([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], True),
    ],
)
def test_is_reflected(points: list[list[int]], expected: bool) -> None:
    assert is_reflected(points) == expected
