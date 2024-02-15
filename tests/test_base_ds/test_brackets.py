import pytest

from base_ds import brackets


@pytest.mark.parametrize(
    "s, expected",
    [
        ("[]", None),
        ("{}", None),
        ("()", None),
        ("{[()]}", None),
        ("{[()]", 1),
        ("{[}", 3),
        ("{", 1),
        ("", None),
    ],
)
def test_brackets(s: str, expected: int):
    assert brackets(s) == expected
