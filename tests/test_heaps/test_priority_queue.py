import pytest

from src.n_heaps.priority_queue import PriorityQueue


def is_max_heap(a: list[int]) -> bool:
    return all(a[i] >= a[2 * i + 1] and (2 * i + 2 >= len(a) or a[i] >= a[2 * i + 2]) for i in range(len(a) // 2))


def test_init_empty_queue() -> None:
    # пустая очередь создаётся без ошибок
    pq = PriorityQueue()

    assert pq.arr == []
    assert pq.size == 0


def test_init_heapifies_array() -> None:
    # при создании из массива он превращается в max-heap
    pq = PriorityQueue([1, 5, 3, 2, 4])

    assert pq.size == 5
    assert is_max_heap(pq.arr)
    assert sorted(pq.arr) == [1, 2, 3, 4, 5]


def test_init_keeps_already_valid_heap() -> None:
    # уже корректная max-heap остаётся валидной
    pq = PriorityQueue([10, 7, 9, 1, 3, 4])

    assert pq.arr == [10, 7, 9, 1, 3, 4]
    assert pq.size == 6
    assert is_max_heap(pq.arr)


def test_swap_changes_two_elements() -> None:
    # swap меняет местами два элемента
    pq = PriorityQueue([3, 2, 1])

    pq.swap(0, 2)

    assert pq.arr == [1, 2, 3]


def test_sift_up_moves_element_to_root() -> None:
    # sift_up поднимает большой элемент до корня
    pq = PriorityQueue([10, 7, 9])
    pq.arr.append(15)
    pq.size += 1

    pq.sift_up(3)

    assert pq.arr[0] == 15
    assert is_max_heap(pq.arr)


def test_sift_up_does_nothing_when_parent_is_larger() -> None:
    # если родитель больше, sift_up ничего не меняет
    pq = PriorityQueue([10, 7, 9])
    before = pq.arr[:]

    pq.sift_up(1)

    assert pq.arr == before
    assert is_max_heap(pq.arr)


def test_sift_up_does_nothing_for_root() -> None:
    # для корня sift_up ничего не делает
    pq = PriorityQueue([10, 7, 9])
    before = pq.arr[:]

    pq.sift_up(0)

    assert pq.arr == before


def test_sift_down_moves_small_root_down() -> None:
    # sift_down опускает слишком маленький корень вниз
    pq = PriorityQueue([10, 9, 8, 7, 6])
    pq.arr[0] = 1

    pq.sift_down(0)

    assert is_max_heap(pq.arr)
    assert pq.arr[0] == 9


def test_sift_down_prefers_right_child_when_right_is_larger() -> None:
    # если правый потомок больше левого, выбирается правый
    pq = PriorityQueue([10, 9, 8])
    pq.arr = [1, 2, 3]
    pq.size = 3

    pq.sift_down(0)

    assert pq.arr == [3, 2, 1]
    assert is_max_heap(pq.arr)


def test_sift_down_prefers_left_child_when_children_are_equal() -> None:
    # если потомки равны, выбирается левый
    pq = PriorityQueue([10, 9, 8])
    pq.arr = [1, 3, 3]
    pq.size = 3

    pq.sift_down(0)

    assert pq.arr == [3, 1, 3]
    assert is_max_heap(pq.arr)


def test_sift_down_stops_when_parent_is_equal_to_child() -> None:
    # если родитель равен максимальному потомку, sift_down останавливается
    pq = PriorityQueue([3, 3, 2])
    before = pq.arr[:]

    pq.sift_down(0)

    assert pq.arr == before
    assert is_max_heap(pq.arr)


def test_insert_into_empty_queue() -> None:
    # вставка в пустую очередь
    pq = PriorityQueue()

    pq.insert(10)

    assert pq.arr == [10]
    assert pq.size == 1
    assert is_max_heap(pq.arr)


def test_insert_small_element_stays_leaf() -> None:
    # маленький элемент остаётся внизу
    pq = PriorityQueue([10, 7, 9])

    pq.insert(1)

    assert pq.size == 4
    assert sorted(pq.arr) == [1, 7, 9, 10]
    assert is_max_heap(pq.arr)


def test_insert_large_element_becomes_root() -> None:
    # большой элемент поднимается в корень
    pq = PriorityQueue([10, 7, 9])

    pq.insert(100)

    assert pq.arr[0] == 100
    assert pq.size == 4
    assert sorted(pq.arr) == [7, 9, 10, 100]
    assert is_max_heap(pq.arr)


def test_insert_duplicates() -> None:
    # дубликаты корректно хранятся в куче
    pq = PriorityQueue([5, 5, 5])

    pq.insert(5)

    assert pq.size == 4
    assert pq.arr == [5, 5, 5, 5]
    assert is_max_heap(pq.arr)


def test_insert_negative_numbers() -> None:
    # отрицательные числа тоже поддерживаются
    pq = PriorityQueue([-10, -20, -30])

    pq.insert(-5)

    assert pq.arr[0] == -5
    assert pq.size == 4
    assert sorted(pq.arr) == [-30, -20, -10, -5]
    assert is_max_heap(pq.arr)


def test_extract_max_from_one_element_queue() -> None:
    # извлечение единственного элемента
    pq = PriorityQueue([42])

    result = pq.extract_max()

    assert result == 42
    assert pq.arr == []
    assert pq.size == 0


def test_extract_max_returns_largest_element() -> None:
    # extract_max возвращает максимум
    pq = PriorityQueue([1, 5, 3, 2, 4])

    result = pq.extract_max()

    assert result == 5
    assert pq.size == 4
    assert sorted(pq.arr) == [1, 2, 3, 4]
    assert is_max_heap(pq.arr)


def test_extract_max_multiple_times_returns_descending_order() -> None:
    # последовательные извлечения возвращают элементы по убыванию
    values = [3, 1, 10, 7, 2, 10, -1]
    pq = PriorityQueue(values)

    extracted = [pq.extract_max() for _ in range(len(values))]

    assert extracted == sorted(values, reverse=True)
    assert pq.arr == []
    assert pq.size == 0


def test_extract_max_with_duplicates() -> None:
    # одинаковые максимумы извлекаются корректно
    pq = PriorityQueue([5, 1, 5, 3])

    assert pq.extract_max() == 5
    assert pq.extract_max() == 5
    assert pq.extract_max() == 3
    assert pq.extract_max() == 1
    assert pq.arr == []
    assert pq.size == 0


def test_extract_max_with_negative_numbers() -> None:
    # максимум среди отрицательных чисел — число ближе к нулю
    pq = PriorityQueue([-10, -1, -5, -20])

    result = pq.extract_max()

    assert result == -1
    assert pq.size == 3
    assert sorted(pq.arr) == [-20, -10, -5]
    assert is_max_heap(pq.arr)


def test_extract_max_from_empty_queue_raises_index_error() -> None:
    # текущая реализация на пустой очереди падает с IndexError
    pq = PriorityQueue()

    with pytest.raises(IndexError):
        pq.extract_max()


def test_heapify_empty_array() -> None:
    # heapify для пустого массива ничего не делает
    pq = PriorityQueue()

    pq.heapify()

    assert pq.arr == []
    assert pq.size == 0


def test_heapify_single_element() -> None:
    # heapify для одного элемента ничего не меняет
    pq = PriorityQueue([1])

    pq.heapify()

    assert pq.arr == [1]
    assert pq.size == 1
    assert is_max_heap(pq.arr)


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3, 4, 5],  # возрастающий массив
        [5, 4, 3, 2, 1],  # убывающий массив
        [4, 1, 3, 2, 16, 9, 10],  # смешанный массив
        [0, -1, -2, -3, -4],  # отрицательные числа
        [2, 2, 2, 2],  # все элементы равны
        [7, 1, 7, 3, 7, 2],  # дубликаты максимумов
    ],
)
def test_priority_queue_general_properties(values: list[int]) -> None:
    # общие свойства очереди:
    # - после heapify структура является max-heap
    # - все элементы сохранены
    # - extract_max возвращает элементы по убыванию
    pq = PriorityQueue(values[:])

    assert is_max_heap(pq.arr)
    assert sorted(pq.arr) == sorted(values)

    extracted = [pq.extract_max() for _ in range(len(values))]

    assert extracted == sorted(values, reverse=True)
    assert pq.arr == []
    assert pq.size == 0
