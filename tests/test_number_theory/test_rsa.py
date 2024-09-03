import pytest

from src.number_theory import generate_keypair, encrypt


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
):
    assert generate_keypair(p, q, e_start) == expected


@pytest.mark.parametrize(
    "plaintext, public_key, expected",
    [
        ("a", (5, 247), [184]),
        ("a", (5, 299), [158]),
        ("abc", (3, 391), [1, 90]),
        ("abc", (3, 551), [122]),
        ("abc", (5, 551), [1, 101]),
    ],
)
def test_encrypt(
    plaintext: str, public_key: tuple[int, int], expected: list[int]
):
    assert encrypt(plaintext, public_key) == expected
