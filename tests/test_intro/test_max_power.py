import pytest

from src.a_intro.max_power import max_power


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("leetcode", 2),
        ("abbcccddddeeeeedcba", 5),
        ("triplepillooooow", 5),
        ("hooraaaaaaaaaaay", 11),
        ("tourist", 1),
    ],
)
def test_max_power(s: str, expected: int) -> None:
    assert max_power(s) == expected
