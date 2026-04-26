from collections.abc import Callable
from typing import Any

import pytest

from src.o_graphs.journey_path import Flight, get_route, get_route_enhanced


@pytest.mark.parametrize("func", [get_route, get_route_enhanced])
@pytest.mark.parametrize(
    ("flights", "expected"),
    [
        ([("Москва", "Белград")], ["Москва", "Белград"]),
        ([("Москва", "Белград"), ("Москва", "Ереван")], ["Ереван", "Москва", "Белград"]),
        (
            [("Ереван", "Москва"), ("Москва", "СПБ"), ("СПБ", "Белград")],
            [
                "Ереван",
                "Москва",
                "СПБ",
                "Белград",
            ],
        ),
    ],
)
def test_journey_path(func: Callable[..., Any], flights: list[Flight], expected: list[str]) -> None:
    assert func(flights) == expected or func(flights) == list(reversed(expected))
