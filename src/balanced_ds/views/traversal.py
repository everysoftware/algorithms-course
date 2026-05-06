from src.balanced_ds.bst.tree import BST


def task_traversal() -> None:
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    for traversal in solve_traversal(n, a):
        print(*traversal)


def solve_traversal(_n: int, a: list[list[int]]) -> list[list[int]]:
    tree = BST[int, None].from_array(a)
    return [
        tree.dfs(style="inorder"),
        tree.dfs(style="preorder"),
        tree.dfs(style="postorder"),
    ]
