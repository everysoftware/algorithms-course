from fib import *
from lis import *


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
    print(lss(a))


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
        s = lis(a)
        print(f'LIS Length: {len(s)}')
        print(f'LIS 1:', *[a[i] for i in s])
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
        ['Task 1. Longest successive subsequence', test_lss],
        ['Task 2. Longest non-increasing subsequence', test_lnis]
        ]
    for i, x in enumerate(f):
        print(f'{i + 1}. {x[0]}')
    f[int(input()) - 1][1]()


main()
