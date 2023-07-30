from bst import make_bst
from avl import make_avl
from bst_test import BSTTest
from traversal import traversal, traversal_iter
from is_bst import is_bst, is_bst_iter, is_general_bst


def test_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    bst_test = BSTTest(make_bst(a))
    bst_test.test_all()


def test_avl():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    bst_test = BSTTest(make_avl(a))
    bst_test.test_all()


def test_dfs():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = make_avl(a)
    for lst in traversal(root):
        print(*lst)


def test_dfs_iter():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = make_avl(a)
    for lst in traversal_iter(root):
        print(*lst)


def test_is_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = make_avl(a)
    print('CORRECT' if is_bst(root) else 'INCORRECT')


def test_is_bst_iter():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = make_avl(a)
    print('CORRECT' if is_bst_iter(root) else 'INCORRECT')


def test_is_general_bst():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    root = make_avl(a)
    print('CORRECT' if is_general_bst(root) else 'INCORRECT')


def main():
    f = [('BST', test_bst),
         ('AVL Tree', test_avl),
         ('Traversal', test_dfs),
         ('Task #1. Iterative traversal', test_dfs_iter),
         ('BST property check', test_is_bst),
         ('Task #2. Iterative BST property check', test_is_bst_iter),
         ('Task #3. General BST property check', test_is_general_bst)]
    for i, x in enumerate(f):
        print(f'{i + 1}. {x[0]}')
    n = int(input())
    if 1 <= n <= len(f):
        f[n - 1][1]()
    else:
        print('Unknown option')


if __name__ == '__main__':
    main()
