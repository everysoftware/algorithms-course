import pytest

from greedy import party_planning


@pytest.mark.parametrize(
    "tree, expected",
    [
        (
            {
                "A": ["B", "C", "D", "L"],
                "B": "E",
                "C": "F",
                "D": ["G", "H"],
                "G": ["I", "J", "K"],
                "J": "M",
            },
            {"A", "M", "G", "H", "F", "E"},
        ),
        (
            {
                "CEO": ["CTO", "CFO"],
                "CTO": ["Engineer1", "Engineer2"],
                "CFO": ["Accountant"],
            },
            {"CEO", "Engineer1", "Engineer2", "Accountant"},
        ),
    ],
)
def test_party_planning(tree: dict[str, list[str]], expected: list[str]):
    assert party_planning(tree) == expected
