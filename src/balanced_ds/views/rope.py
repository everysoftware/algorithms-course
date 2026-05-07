from src.balanced_ds.rope import Rope


def task_rope() -> None:
    s = input()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    print(solve_rope(s, queries))


def solve_rope(s: str, queries: list[list[int]]) -> str:
    r = Rope.from_string(s)
    for i, j, k in queries:
        r.move_substr(i, j, k)
    return r.to_string()
