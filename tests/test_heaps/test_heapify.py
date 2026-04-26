import pytest

from src.n_heaps.heapify import heapify


def is_min_heap(a: list[int]) -> bool:
    return all(a[i] <= a[2 * i + 1] and (2 * i + 2 >= len(a) or a[i] <= a[2 * i + 2]) for i in range(len(a) // 2))


def replay_swaps(original: list[int], swaps: list[tuple[int, int]]) -> list[int]:
    a = original[:]
    for i, j in swaps:
        a[i], a[j] = a[j], a[i]
    return a


@pytest.mark.parametrize(
    ("a", "expected_swaps", "expected_heap"),
    [
        ([], [], []),  # пустой массив → никаких свапов, результат тот же
        ([1], [], [1]),  # один элемент → куча уже валидна
        ([1, 2], [], [1, 2]),  # уже min-heap → изменений нет
        ([2, 1], [(0, 1)], [1, 2]),  # два элемента в обратном порядке → один свап
        ([1, 2, 3], [], [1, 2, 3]),  # уже корректная куча
        ([3, 2, 1], [(0, 2)], [1, 2, 3]),  # выбирается правый ребёнок (он меньше)
        ([3, 1, 2], [(0, 1)], [1, 3, 2]),  # выбирается левый ребёнок
        ([5, 4, 3, 2, 1], [(1, 4), (0, 1), (1, 3)], [1, 2, 3, 5, 4]),  # несколько sift_down
        ([5, 5, 5], [], [5, 5, 5]),  # все элементы равны → свапов нет
        ([2, 2, 1], [(0, 2)], [1, 2, 2]),  # равные + меньший правый ребёнок
        ([0, -1, -2, -3], [(1, 3), (0, 1), (1, 3)], [-3, -1, -2, 0]),  # отрицательные числа
    ],
)
def test_heapify_exact_cases(a: list[int], expected_swaps: list[tuple[int, int]], expected_heap: list[int]) -> None:
    # проверяем точные сценарии: последовательность свапов и финальное состояние
    original = a[:]

    swaps = heapify(len(a), a)

    assert swaps == expected_swaps
    assert a == expected_heap
    assert is_min_heap(a)
    assert replay_swaps(original, swaps) == a


def test_heapify_ignores_elements_after_size() -> None:
    # heapify должен работать только на первых size элементах
    a = [5, 4, 3, 2, 1, -100, -200]

    swaps = heapify(5, a)

    assert swaps == [(1, 4), (0, 1), (1, 3)]
    assert a == [1, 2, 3, 5, 4, -100, -200]
    assert is_min_heap(a[:5])
    assert a[5:] == [-100, -200]


def test_heapify_size_smaller_than_zero_swaps_nothing() -> None:
    # если size = 0 → функция не должна ничего менять
    a = [3, 2, 1]

    swaps = heapify(0, a)

    assert swaps == []
    assert a == [3, 2, 1]


def test_heapify_returns_empty_for_already_valid_heap() -> None:
    # если массив уже min-heap → никаких свапов не происходит
    a = [1, 3, 2, 7, 6, 4, 5]

    swaps = heapify(len(a), a)

    assert swaps == []
    assert a == [1, 3, 2, 7, 6, 4, 5]
    assert is_min_heap(a)


@pytest.mark.parametrize(
    "a",
    [
        [7, 6, 5, 4, 3, 2, 1],
        [10, 9, 8, 7, 6, 5, 4, 3],
        [4, 1, 3, 2, 16, 9, 10, 14, 8, 7],
        [3, 1, 1, 0, 2, 2, -1],
    ],
)
def test_heapify_general_properties(a) -> None:
    # проверяем общие свойства:
    # - результат является min-heap
    # - элементы не теряются
    # - свапы корректно воспроизводят результат
    original = a[:]

    swaps = heapify(len(a), a)

    assert is_min_heap(a)
    assert sorted(a) == sorted(original)
    assert replay_swaps(original, swaps) == a
    assert all(0 <= i < len(a) and 0 <= j < len(a) for i, j in swaps)


def test_heapify_prefers_right_child_when_right_is_smaller() -> None:
    # если правый ребёнок меньше левого → выбирается правый
    a = [3, 2, 1]

    swaps = heapify(len(a), a)

    assert swaps == [(0, 2)]
    assert a == [1, 2, 3]


def test_heapify_prefers_left_child_when_children_are_equal() -> None:
    # если дети равны → выбирается левый (по коду)
    a = [3, 1, 1]

    swaps = heapify(len(a), a)

    assert swaps == [(0, 1)]
    assert a == [1, 3, 1]


def test_heapify_stops_when_parent_equals_child() -> None:
    # если родитель <= ребёнка → sift_down останавливается
    a = [1, 1, 2]

    swaps = heapify(len(a), a)

    assert swaps == []
    assert a == [1, 1, 2]
