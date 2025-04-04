import pytest

from src.f_scanline.max_profit import job_scheduling


@pytest.mark.parametrize(
    ("start_time", "end_time", "profit", "expected"),
    [
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
        ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6),
    ],
)
def test_job_scheduling(start_time: list[int], end_time: list[int], profit: list[int], expected: int) -> None:
    assert job_scheduling(start_time, end_time, profit) == expected
