from src.dsu.max_dsu import MaxDSU


def table_union(sizes: list[int], queries: list[tuple[int, int]]) -> list[int]:
    result: list[int] = []
    s = MaxDSU(sizes)
    for i in range(len(queries)):
        s.union(queries[i][0] - 1, queries[i][1] - 1)
        result.append(s.curr_max)
    return result
