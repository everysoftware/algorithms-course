import pytest

from src.dsu.dsu import DSU, ArrayDSU, CompressedForestDSU, ForestDSU

DSU_CLASSES: list[type[DSU]] = [ArrayDSU, ForestDSU, CompressedForestDSU]


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_make_set_and_find_singletons(cls: type[DSU]) -> None:
    dsu = cls(5)

    for i in range(1, 6):
        dsu.make_set(i)

    for i in range(1, 6):
        assert dsu.find(i) == i


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_union_two_elements(cls: type[DSU]) -> None:
    dsu = cls(5)
    for i in range(1, 6):
        dsu.make_set(i)

    dsu.union(1, 2)

    assert dsu.find(1) == dsu.find(2)
    assert dsu.find(3) == 3
    assert dsu.find(4) == 4
    assert dsu.find(5) == 5


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_union_chain(cls: type[DSU]) -> None:
    dsu = cls(5)
    for i in range(1, 6):
        dsu.make_set(i)

    dsu.union(1, 2)
    dsu.union(2, 3)
    dsu.union(3, 4)

    root = dsu.find(1)
    assert dsu.find(2) == root
    assert dsu.find(3) == root
    assert dsu.find(4) == root
    assert dsu.find(5) != root


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_union_two_sets(cls: type[DSU]) -> None:
    dsu = cls(6)
    for i in range(1, 7):
        dsu.make_set(i)

    dsu.union(1, 2)
    dsu.union(3, 4)
    dsu.union(2, 3)

    root = dsu.find(1)
    assert dsu.find(2) == root
    assert dsu.find(3) == root
    assert dsu.find(4) == root

    assert dsu.find(5) == 5
    assert dsu.find(6) == 6


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_repeated_union_does_not_break_structure(cls: type[DSU]) -> None:
    dsu = cls(4)
    for i in range(1, 5):
        dsu.make_set(i)

    dsu.union(1, 2)
    root = dsu.find(1)

    dsu.union(1, 2)
    dsu.union(2, 1)
    dsu.union(1, 1)

    assert dsu.find(1) == root
    assert dsu.find(2) == root
    assert dsu.find(3) == 3
    assert dsu.find(4) == 4


def test_array_dsu_set_id_is_minimum_element() -> None:
    dsu = ArrayDSU(9)
    for i in range(1, 10):
        dsu.make_set(i)

    dsu.union(9, 3)
    dsu.union(3, 2)
    dsu.union(2, 4)
    dsu.union(4, 7)
    dsu.union(6, 1)
    dsu.union(1, 8)

    assert dsu.smallest == [0, 1, 2, 2, 2, 5, 1, 2, 1, 2]

    for i in [9, 3, 2, 4, 7]:
        assert dsu.find(i) == 2

    assert dsu.find(5) == 5

    for i in [6, 1, 8]:
        assert dsu.find(i) == 1


def test_forest_dsu_parent_and_rank_after_known_unions() -> None:
    dsu = ForestDSU(9)
    for i in range(1, 10):
        dsu.make_set(i)

    dsu.union(9, 3)
    dsu.union(3, 2)
    dsu.union(2, 4)
    dsu.union(4, 7)
    dsu.union(6, 1)
    dsu.union(1, 8)

    assert dsu.parent == [0, 1, 3, 3, 3, 5, 1, 3, 1, 3]
    assert dsu.rank == [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]


def test_forest_dsu_union_by_rank_when_left_rank_greater() -> None:
    dsu = ForestDSU(4)
    for i in range(1, 5):
        dsu.make_set(i)

    dsu.union(1, 2)
    dsu.union(3, 2)

    root = dsu.find(1)

    assert dsu.find(2) == root
    assert dsu.find(3) == root
    assert dsu.rank[root] == 1


def test_forest_dsu_rank_increases_only_for_equal_ranks() -> None:
    dsu = ForestDSU(4)
    for i in range(1, 5):
        dsu.make_set(i)

    dsu.union(1, 2)
    root = dsu.find(1)

    assert dsu.rank[root] == 1

    dsu.union(3, 1)

    assert dsu.find(3) == root
    assert dsu.rank[root] == 1


def test_compressed_forest_find_compresses_path() -> None:
    dsu = CompressedForestDSU(5)
    for i in range(1, 6):
        dsu.make_set(i)

    dsu.parent[1] = 2
    dsu.parent[2] = 3
    dsu.parent[3] = 4
    dsu.parent[4] = 5
    dsu.parent[5] = 5

    assert dsu.find(1) == 5

    assert dsu.parent[1] == 5
    assert dsu.parent[2] == 5
    assert dsu.parent[3] == 5
    assert dsu.parent[4] == 5
    assert dsu.parent[5] == 5


def test_compressed_forest_find_on_root_keeps_root() -> None:
    dsu = CompressedForestDSU(3)
    for i in range(1, 4):
        dsu.make_set(i)

    assert dsu.find(2) == 2
    assert dsu.parent[2] == 2


@pytest.mark.parametrize("cls", DSU_CLASSES)
def test_all_elements_can_be_merged_into_one_set(cls: type[DSU]) -> None:
    dsu = cls(10)
    for i in range(1, 11):
        dsu.make_set(i)

    for i in range(1, 10):
        dsu.union(i, i + 1)

    root = dsu.find(1)

    for i in range(1, 11):
        assert dsu.find(i) == root


def test_array_dsu_union_uses_minimum_id_after_merging_sets() -> None:
    dsu = ArrayDSU(6)
    for i in range(1, 7):
        dsu.make_set(i)

    dsu.union(4, 6)
    dsu.union(2, 3)
    dsu.union(6, 3)

    for i in [2, 3, 4, 6]:
        assert dsu.find(i) == 2

    assert dsu.find(1) == 1
    assert dsu.find(5) == 5
