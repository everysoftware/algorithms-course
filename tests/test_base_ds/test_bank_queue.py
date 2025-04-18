import pytest

from src.b_base_ds.bank_queue import average_waiting_time


@pytest.mark.parametrize(
    ("n", "clients", "expected"),
    [
        (2, [(1, 10), (2, 5), (3, 7)], 1.333333),
        (1, [(1, 1), (2, 1), (3, 1)], 0),
        (1, [(1, 1)], 0),
        (2, [(1, 0), (2, 0), (3, 0)], 0),
    ],
)
def test_average_waiting_time(n: int, clients: list[tuple[int, int]], expected: float) -> None:
    assert average_waiting_time(n, clients) == expected
