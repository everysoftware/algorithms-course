from brackets import *
from max_stack import *
from net_packets import *
from tree_height import *
from sliding_window import *


def test_sliding_window():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    print(*sliding_window(n, a, m))


def test_tree_height():
    _ = int(input())
    a = list(map(int, input().split()))
    print(tree_height(a))


def test_net_packets():
    size, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    arrival = [x[0] for x in data]
    duration = [x[1] for x in data]
    print(*net_packets(size, n, arrival, duration), sep='\n')


def test_max_stack():
    st = MaxStack()
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'push':
            st.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            st.pop()
        elif cmd[0] == 'max':
            print(st.max())


def test_brackets():
    s = input()
    result = brackets_improved(s)
    print('Success' if result == -1 else result)


def main():
    a = [
        ('Task #1. Check brackets', test_brackets),
        ('Task #2. Tree height', test_tree_height),
        ('Task #3. Net packets', test_net_packets),
        ('Task #4. Max stack', test_max_stack),
        ('Task #5. Sliding window', test_sliding_window)
    ]
    for i, x in enumerate(a):
        print(f'{i + 1}. {x[0]}')
    n = int(input('Enter command: '))
    if n > len(a):
        print('Unknown command')
    else:
        a[n - 1][1]()


main()
