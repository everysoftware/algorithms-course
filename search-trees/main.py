from bst import BST
from bst_test import BSTTest

from avl import AVLTree
from avl_test import AVLTest

from traversal import traversal, traversal_iter
from is_bst import is_bst, is_bst_iter, is_general_bst


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


def main():
    f = [('Test BST', test_bst),
         ('Test AVL Tree', test_avl),
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
