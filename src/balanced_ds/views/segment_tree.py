from typing import Any

from src.balanced_ds.segment_tree import IntSegmentTree


def task_segment_tree() -> None:
    n = int(input())
    queries = [input().split() for _ in range(n)]

    for _, ans in solve_segment_tree(queries):
        print(ans)


def solve_segment_tree(queries: list[list[str]]) -> list[tuple[Any, ...]]:
    tree = IntSegmentTree()
    s = 0

    def f(x: int) -> int:
        return (x + s) % 1_000_000_001

    result: list[tuple[Any, ...]] = []

    for i, args in enumerate(queries):
        option = args[0]
        if option == "?":
            key = f(int(args[1]))
            result.append((i + 1, "Found" if tree.contains(key) else "Not found"))
        elif option == "+":
            key = f(int(args[1]))
            tree.insert(key)
        elif option == "s":
            left, right = f(int(args[1])), f(int(args[2]))
            s = tree.sum_between(left, right)
            result.append((i + 1, s))
        elif option == "-":
            key = f(int(args[1]))
            tree.delete(key)

    return result
