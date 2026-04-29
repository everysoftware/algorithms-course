from src.dsu.dsu import CompressedForestDSU


def auto_analysis(n: int, e: int, d: int, equals: list[tuple[int, int]], not_equals: list[tuple[int, int]]) -> bool:
    s = CompressedForestDSU(n)
    for i in range(1, n + 1):
        s.make_set(i)
    for i in range(e):
        s.union(equals[i][0], equals[i][1])
    return all(s.find(not_equals[i][0]) != s.find(not_equals[i][1]) for i in range(d))
