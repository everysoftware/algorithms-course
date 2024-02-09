from binary_search import *
from divide_and_conquer.algo.integer_multiplication import *
from divide_and_conquer.algo.matrix_multiplication import *
from src.sortings.sorting import *
from divide_and_conquer.algo.inv_count import *
from divide_and_conquer.algo.points_and_segments import *
from divide_and_conquer.algo.rec_analyze import *


def test_rec_solve():
    relations = [
        [2, 2, 1],
        [5, 4, 1],
        [1, 2, 0],
        [3, 2, 1],
        [5, 2, 1],
        [5, 4, 2],
        [6, 4, 3],
        [9, 3, 2],
        [2, 3, 0]
    ]
    result = sorted(relations, key=rec_analyze)
    print('In ascending order:')
    for x in result:
        a, b, d = x
        print(f'T(n) = {a}T(n/{b}) + O(n^{d}) = {rec_analyze_str(x)}')


def test_count_sort():
    _ = int(input())
    a = list(map(int, input().split()))
    print(*count_sort(a))


"""
Точка считается принадлежащей отрезку, если она находится внутри него или на границе. 
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""


def test_points_and_segments():
    n, m = map(int, input().split())
    segments = [list(map(int, input().split())) for _ in range(n)]
    points = list(map(int, input().split()))
    print(*points_and_segments(segments, points))


def test_inverse_count():
    n = int(input())
    a = list(map(int, input().split()))
    print(inverse_count(a))


def test_sorting():
    tests = [[10, 40, 50, 60, 95],
             [95, 60, 50, 40, 10],
             [40, 50, 95, 10, 60],
             [7, 2, 5, 3, 7, 13, 1, 6],
             [],
             [0],
             [7, 7, 7, 7, 7, 7, 7, 7, 7],
             [267, 507, 912, 215, 109, 213, 199, 216, 257]]
    for i, test in enumerate(tests):
        print(f'TEST #{i + 1}')
        print('Source array:', *test)
        print('Sorted array (by insertion sort)   :', *insertion_sort(test.copy()))
        print('Sorted array (by merge sort)       :', *merge_sort(test, 0, len(test) - 1))
        print('Sorted array (by iter merge sort)  :', *iterative_merge_sort(test))
        print('Sorted array (by quick sort)       :', *quick_sort(test.copy(), 0, len(test) - 1))
        print('Sorted array (by quick sort3)      :', *quick_sort3(test.copy(), 0, len(test) - 1))
        print('Sorted array (by selection sort)   :', *selection_sort(test))
        print('Sorted array (by heap sort)        :', *heap_sort(test))
        print('Sorted array (by heap sort inplace):', *heap_sort_inplace(test.copy()))
        print('Sorted array (by count sort)       :', *count_sort(test, 10 ** 3))
        print('Sorted array (by digit sort)       :', *digit_sort(test))
        print('Random select (all indices)        :',
              *[random_select(test.copy(), 0, len(test) - 1, j) for j in range(len(test))])
        print()


def test_matrix_multiply():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
    print(f'A\n{matrix_to_str(a)}')
    print('x')
    print(f'B\n{matrix_to_str(b)}')
    print('=')
    print(f'Naive\n{matrix_to_str(matrix_multiply_naive(a, b))}')


def test_multiply():
    # x, y = map(int, input().split())
    x, y = 9874563256487921, 152458796389852357456
    print(f'Naive:\n{x} * {y} = {multiply_naive(x, y)}')
    print(f'Intermediate:\n{x} * {y} = {multiply_intermediate(x, y)}')
    print(f'Karatsuba:\n{x} * {y} = {karatsuba(x, y)}')


def test_binary_search():
    a = list(map(int, input().split()))[1:]
    tests = list(map(int, input().split()))[1:]
    result = []
    for x in tests:
        i = binary_search(a, x)
        result.append(-1 if a[i] != x else i + 1)
    print(*result)


def main():
    f = [
        ['Task 1. Binary search', test_binary_search],
        ['Integers multiplication test', test_multiply],
        ['Matrix multiplication test', test_matrix_multiply],
        ['Sorting test', test_sorting],
        ['Task 2. Inverse count', test_inverse_count],
        ['Task 3. Points and segments', test_points_and_segments],
        ['Task 4. Count sort', test_count_sort],
        ['Task 5. Recursive algorithm analyze', test_rec_solve]
    ]
    for i, x in enumerate(f):
        print(f'{i + 1}: {x[0]}')
    f[int(input()) - 1][1]()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
