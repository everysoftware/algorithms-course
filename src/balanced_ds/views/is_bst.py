from src.balanced_ds.bst.tree import BST
from src.balanced_ds.bst.utils import is_bst, is_general_bst


def task_is_bst() -> None:
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    tree = BST[int, None].from_array(a)

    print("CORRECT" if is_bst(tree.root) else "INCORRECT")


def task_is_general_bst() -> None:
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    tree = BST[int, None].from_array(a)

    print("CORRECT" if is_general_bst(tree.root) else "INCORRECT")
