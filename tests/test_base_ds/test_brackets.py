import pytest

from src.b_base_ds.brackets import brackets


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
def test_brackets(s: str, expected: int) -> None:
    assert brackets(s) == expected
