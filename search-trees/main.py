from bst import BST
from bst_test import BSTTest
from avl_tree import AVLTree
from avl_test import AVLTest
from traversal import traversal, traversal_iter
from is_bst import is_bst, is_bst_iter, is_general_bst
from accumulative_set import accumulative_set
from rope import rope


def test_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    BSTTest(BST().build_from_array(a)).test_all()


def test_avl():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    AVLTest(AVLTree().build_from_array(a)).test_all()


def test_dfs():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = BST().build_from_array(a).root
    for lst in traversal(root):
        print(*lst)


def test_dfs_iter():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = BST().build_from_array(a).root
    for lst in traversal_iter(root):
        print(*lst)


def test_is_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = BST().build_from_array(a).root
    print('CORRECT' if is_bst(root) else 'INCORRECT')


def test_is_bst_iter():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = BST().build_from_array(a).root
    print('CORRECT' if is_bst_iter(root) else 'INCORRECT')


def test_is_general_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = BST().build_from_array(a).root
    print('CORRECT' if is_general_bst(root) else 'INCORRECT')


def test_accumulative_set():
    n = int(input())
    queries = [input().split() for _ in range(n)]
    for _, ans in accumulative_set(queries):
        print(ans)


def test_rope():
    s = input()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    print(rope(s, queries))


def main():
    options = [
        ('Test BST', test_bst),
        ('Test AVL Tree', test_avl),
        ('Traversal', test_dfs),
        ('Iterative traversal (Task #1)', test_dfs_iter),
        ('BST property check', test_is_bst),
        ('Iterative BST property check (Task #2)', test_is_bst_iter),
        ('General BST property check (Task #3)', test_is_general_bst),
        ('Accumulative set (Task #4)', test_accumulative_set),
        ('Rope (Task #5)', test_rope)
    ]
    for i, option in enumerate(options):
        print(f'{i + 1}. {option[0]}')
    option_number = int(input())
    if 1 <= option_number <= len(options):
        options[option_number - 1][1]()
    else:
        print('Unknown option')


if __name__ == '__main__':
    main()
