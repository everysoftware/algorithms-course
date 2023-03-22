from points_cover import *
from act_sel import *
from max_independent_set import *
from min_set_of_points import *
from knapsack import *
from max_terms import *
from huffman import *
from priority_queue import *


def test_priority_queue():
    q = PriorityQueue()
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'Insert':
            q.insert(int(cmd[1]))
        elif cmd[0] == 'ExtractMax':
            print(q.extract_max())


"""
Кодирование строки
"""


def test_huffman_decoding():
    n, _ = map(int, input().split())
    d = {}
    for _ in range(n):
        letter, code = input().split(': ')
        d[code] = letter
    encoded_s = input()
    decoded_s = huffman_decode(encoded_s, d)
    print(decoded_s)


def test_huffman():
    s = input()
    tree = huffman_tree(s)
    table = {c: x for c, x in tree.items() if len(c) == 1}
    encoded_s = huffman_encode(s, tree)
    print(len(table), len(encoded_s))
    for c, x in table.items():
        print(f'{c}: {x}')
    print(encoded_s)


def test_max_terms():
    n = int(input())
    terms = max_terms(n)
    print('Максимальное количество различных слагаемых:', len(terms))
    print(*terms)


"""
Первая строка содержит количество предметов и вместимость рюкзака.
Каждая из следующих n строк задаёт стоимость и объём предмета.
Выведите максимальную стоимость частей предметов 
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""


def test_knapsack():
    n, w = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]
    result = knapsack(n, w, items)
    print('Макс. стоимость предметов:')
    max_cost = sum(x[1] for x in result)
    print(f'{max_cost:.3f}')
    print(*result)


def test_min_set_of_points():
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    sol = min_set_of_points(segments)
    print(len(sol))
    print(*sol)


def test_max_independent_set():
    tree = {'A': ['B', 'C', 'D', 'L'], 'B': 'E', 'C': 'F', 'D': ['G', 'H'], 'G': ['I', 'J', 'K'], 'J': 'M'}
    print(max_independent_set(tree))  # ['L', 'E', 'F', 'H', 'I', 'K', 'M']


def test_act_sel():
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    sol = act_sel(segments)
    print(f'Максимальное количество непересекающихся отрезков: {len(sol)}')
    print(*sol)


def test_points_cover():
    s = list(map(float, input().split()))
    print('Обычный алгоритм')
    sol = points_cover(s)
    print(f'Минимальное количество отрезков: {len(sol)}')
    print(*sol, sep=', ')
    print('Улучшенный алгоритм')
    sol = points_cover_enhanced(s)
    print(f'Минимальное количество отрезков: {len(sol)}')
    print(*sol, sep=', ')


def main():
    tests = [
        ['Test points cover', test_points_cover],
        ['Test act sel', test_act_sel],
        ['Test max independent set', test_max_independent_set],
        ['Task 1 (min set of points)', test_min_set_of_points],
        ['Task 2 (continuous backpack)', test_knapsack],
        ['Task 3 (max terms)', test_max_terms],
        ['Task 4 (huffman encoding)', test_huffman],
        ['Task 5 (huffman decoding)', test_huffman_decoding],
        ['Task 6 (priority queue)', test_priority_queue]
    ]
    for i, (s, f) in enumerate(tests):
        print(str(i + 1) + '.', s)
    tests[int(input()) - 1][1]()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
