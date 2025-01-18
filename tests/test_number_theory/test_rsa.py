import pytest

from src.number_theory.rsa import generate_keypair, encrypt


@pytest.mark.parametrize(
    "p, q, e_start, expected",
    [
        (13, 19, 2, ((5, 247), (173, 247))),
        (13, 23, 2, ((5, 299), (53, 299))),
        (17, 23, 2, ((3, 391), (235, 391))),
        (19, 29, 2, ((5, 551), (101, 551))),
    ],
)
def test_generate_keypair(
    p: int,
    q: int,
    e_start: int,
    expected: tuple[tuple[int, int], tuple[int, int]],
) -> None:
    assert generate_keypair(p, q, e_start) == expected


@pytest.mark.parametrize(
    "p, q, e_start, plaintext, expected",
    [
        (13, 19, 2, "a", [184]),
        (13, 23, 2, "a", [158]),
        (17, 23, 2, "abc", [1, 90]),
        (19, 29, 2, "abc", [1, 101]),
    ],
)
def test_encrypt(p: int, q: int, e_start: int, plaintext: str, expected: list[int]) -> None:
    assert encrypt(p, q, e_start, plaintext) == expected
