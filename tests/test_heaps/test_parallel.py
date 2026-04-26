import pytest

from src.n_heaps.parallel import parallel


def test_parallel_sample_1() -> None:
    # пример 1 из условия: разные времена задач, 2 процессора
    assert parallel(2, 5, [1, 2, 3, 4, 5]) == [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 2),
        (0, 4),
    ]


def test_parallel_sample_2() -> None:
    # пример 2 из условия: 4 процессора, все задачи длятся 1
    assert parallel(4, 20, [1] * 20) == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
    ]


def test_parallel_one_processor() -> None:
    # один процессор: все задачи выполняются строго последовательно
    assert parallel(1, 5, [3, 2, 4, 1, 5]) == [
        (0, 0),
        (0, 3),
        (0, 5),
        (0, 9),
        (0, 10),
    ]


def test_parallel_more_processors_than_tasks() -> None:
    # процессоров больше, чем задач: каждая задача стартует в 0
    assert parallel(5, 3, [10, 20, 30]) == [
        (0, 0),
        (1, 0),
        (2, 0),
    ]


def test_parallel_processors_equal_tasks() -> None:
    # процессоров столько же, сколько задач: все задачи стартуют в 0
    assert parallel(3, 3, [5, 1, 10]) == [
        (0, 0),
        (1, 0),
        (2, 0),
    ]


def test_parallel_zero_duration_tasks() -> None:
    # задачи длительностью 0 не увеличивают время освобождения процессора
    assert parallel(2, 5, [0, 0, 0, 0, 0]) == [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]


def test_parallel_mixed_zero_and_positive_tasks() -> None:
    # нулевые задачи сразу освобождают процессор и влияют на выбор по номеру
    assert parallel(2, 6, [0, 5, 0, 2, 1, 0]) == [
        (0, 0),
        (0, 0),
        (1, 0),
        (1, 0),
        (1, 2),
        (1, 3),
    ]


def test_parallel_tie_choose_smallest_processor_id() -> None:
    # если несколько процессоров свободны одновременно, выбирается меньший номер
    assert parallel(3, 6, [2, 2, 2, 1, 1, 1]) == [
        (0, 0),
        (1, 0),
        (2, 0),
        (0, 2),
        (1, 2),
        (2, 2),
    ]


def test_parallel_tie_after_different_durations() -> None:
    # проверяем tie-breaker после задач разной длины
    assert parallel(2, 5, [5, 1, 4, 1, 1]) == [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 5),
        (1, 5),
    ]


def test_parallel_large_values() -> None:
    # большие значения времени не должны ломать вычисления
    assert parallel(2, 4, [10**9, 10**9, 10**9, 10**9]) == [
        (0, 0),
        (1, 0),
        (0, 10**9),
        (1, 10**9),
    ]


def test_parallel_empty_time_but_m_zero() -> None:
    # формально по условию m >= 1, но функция корректно возвращает пустой ответ при m = 0
    assert parallel(3, 0, []) == []


def test_parallel_uses_only_first_m_tasks() -> None:
    # функция обрабатывает только первые m элементов списка time
    assert parallel(2, 3, [1, 2, 3, 100, 200]) == [
        (0, 0),
        (1, 0),
        (0, 1),
    ]


def test_parallel_raises_if_m_greater_than_time_length() -> None:
    # если m больше длины time, текущая реализация падает с IndexError
    with pytest.raises(IndexError):
        parallel(2, 3, [1, 2])


def test_parallel_raises_if_no_processors() -> None:
    # если n = 0, куча пустая, heappop падает с IndexError
    with pytest.raises(IndexError):
        parallel(0, 1, [10])


@pytest.mark.parametrize(
    ("n", "time", "expected"),
    [
        (
            2,
            [1, 1, 1, 1],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
        ),
        (
            3,
            [3, 1, 2, 1, 1],
            [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],
        ),
        (
            4,
            [2, 4, 1, 3, 5, 2],
            [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1), (0, 2)],
        ),
    ],
)
def test_parallel_exact_cases(n, time, expected) -> None:
    # несколько точных сценариев для разных n и длительностей задач
    assert parallel(n, len(time), time) == expected


@pytest.mark.parametrize(
    ("n", "time"),
    [
        (1, [1, 2, 3, 4]),
        (2, [5, 0, 2, 0, 3]),
        (3, [1, 1, 1, 1, 1, 1, 1]),
        (4, [10, 1, 7, 3, 0, 2, 8]),
        (5, [0, 0, 5, 5, 1, 1, 10]),
    ],
)
def test_parallel_general_properties(n, time) -> None:
    # общие инварианты:
    # - ответ имеет длину m
    # - номера процессоров в допустимом диапазоне
    # - время старта неотрицательное
    # - каждый процессор получает задачи в неубывающем порядке времени старта
    result = parallel(n, len(time), time)

    assert len(result) == len(time)
    assert all(0 <= processor < n for processor, _ in result)
    assert all(start_time >= 0 for _, start_time in result)

    starts_by_processor: dict[int, list[int]] = {}
    for processor, start_time in result:
        starts_by_processor.setdefault(processor, []).append(start_time)

    for starts in starts_by_processor.values():
        assert starts == sorted(starts)


def test_parallel_input_list_is_not_modified() -> None:
    # функция не должна изменять список длительностей задач
    time = [3, 1, 2, 4]
    original = time[:]

    parallel(2, len(time), time)

    assert time == original
