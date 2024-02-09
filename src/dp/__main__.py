from fib import *
from lis import *
from editing import *
from knapsack import *
from dp.algo.matrix_seq_mult import *
from src.dp import *


def test_calc():
    n = int(input())
    s = calc(n)
    print(len(s) - 1)
    print(*s)


def test_ladder():
    _ = int(input())
    a = list(map(int, input().split()))
    print(ladder(a))


def test_matrix_mult_test():
    m = [50, 20, 1, 10, 100]
    print(matrix_mult_td(m))
    print(matrix_mult_bu(m))


def test_golden_knapsack():
    w, n = map(int, input().split())
    weight = list(map(int, input().split()))
    print(golden_knapsack(w, n, weight))


"""
10 4
6 3 4 2
30 14 16 9
"""


def test_knapsack():
    w, n = map(int, input().split())
    weight = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(knapsack_with_reps_bu(w, n, weight, cost))
    print(knapsack_td(w, n, weight, cost))
    print(knapsack_without_reps_bu(w, n, weight, cost))


def test_edit_dist_task():
    a = input()
    b = input()
    print(edit_distance_bu(a, b))


def test_edit_dist():
    tests = [
        ['editing', 'distance'],
        ['short', 'ports']
        ]
    for k, (a, b) in enumerate(tests):
        print(f'TEST #{k + 1}')
        print(f'A = {a}')
        print(f'B = {b}')
        print(f'Editing distance TD: {edit_distance_td(a, b)}')
        print(f'Editing distance BU: {edit_distance_bu(a, b)}')
        print(f'Editing path BU:')
        for num, (t, i, j) in enumerate(edit_path_bu(a, b)):
            if t == 0:
                print(f'{num + 1} - Deleting (\'{a[i]}\' on pos {i + 1})')
            elif t == 1:
                print(f'{num + 1} - Insertion (\'{b[j]}\' on pos {i + 1})')
            else:
                print(f'{num + 1} - Substitution (\'{a[i]}\' on pos {i + 1} by \'{b[j]}\')')
        print()


# Наибольшая невозрастающая последовательность
def test_lnis():
    _ = int(input())
    a = list(map(int, input().split()))
    result = lnis(a)
    print(len(result))
    print(*[i + 1 for i in result])


# Наибольшая последовательно кратная подпоследовательность
def test_lss():
    _ = int(input())
    a = list(map(int, input().split()))
    print(lss_length(a))


def test_lis():
    tests = [
        [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1],
        [2, 5, 3, 7, 11, 8, 10, 13, 6],
        [],
        [7]
    ]
    for i, a in enumerate(tests):
        print(f'TEST #{i + 1}')
        print('Source array:', *a)
        print(f'LIS Length: {lis_length(a)}')
        print(f'LIS Length Improved: {lis_length_improved(a)}')
        print(f'LIS:', *[a[i] for i in lis(a)])
        print(f'LIS 2:', *[a[i] for i in lis2(a)])
        print(f'LIS Improved:', *[a[i] for i in lis_improved(a)])
        print()


def test_fib():
    for i in range(15):
        print(f'{i} => {fib(i)} | {fib_td(i)} | {fib_bu(i)} | {fib_bu_improved(i)}')


def main():
    f = [
        ['Fibonacci numbers', test_fib],
        ['LIS', test_lis],
        ['Task #1. Longest successive subsequence', test_lss],
        ['Task #2. Longest non-increasing subsequence', test_lnis],
        ['Editing distance', test_edit_dist],
        ['Task #3. Editing distance', test_edit_dist_task],
        ['Knapsack', test_knapsack],
        ['Task #4. Golden knapsack', test_golden_knapsack],
        ['Matrix sequence multiplication order', test_matrix_mult_test],
        ['Task #5. Ladder', test_ladder],
        ['Task #6. Calculator', test_calc]
        ]
    for i, x in enumerate(f):
        print(f'{i + 1}. {x[0]}')
    f[int(input()) - 1][1]()


main()
