import pytest

from src.b_base_ds import MaxStack


@pytest.mark.parametrize(
    "operations, expected",
    [
        (
            [
                ("push", 2),
                ("push", 1),
                ("get_max",),
                ("pop",),
                ("get_max",),
                ("push", 3),
                ("get_max",),
            ],
            [2, 2, 3],
        ),
        (
            [
                ("push", 1),
                ("push", 2),
                ("push", 3),
                ("get_max",),
                ("pop",),
                ("get_max",),
            ],
            [3, 2],
        ),
        (
            [
                ("push", 1),
                ("push", 2),
                ("push", 3),
                ("get_max",),
                ("pop",),
                ("get_max",),
                ("pop",),
                ("get_max",),
            ],
            [3, 2, 1],
        ),
    ],
)
def test_max_stack(operations: list[tuple], expected: list[int]):
    stack = MaxStack()

    for op, *args in operations:
        if op == "push":
            stack.push(*args)
        elif op == "pop":
            stack.pop()
        elif op == "get_max":
            assert stack.max() == expected.pop(0)
        else:
            raise ValueError(f"Unknown operation: {op}")

    assert not expected
