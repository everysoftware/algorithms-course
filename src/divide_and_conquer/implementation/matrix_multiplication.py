# наивный алгоритм за O(N^3)
def matrix_multiply_naive(a, b):
    n = len(a)  # к-во строк A
    m = len(b[0])  # к-во столбцов B
    s = len(b)  # к-во строчек B
    assert s == len(a[0])  # необходимое условие
    # A_{n x s} x B_{s, m} = C_{n, m}
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(s):
                c[i][j] += a[i][k] * b[k][j]
    return c


# всё ещё за O(N^3), но скоро будет лучше :)
# к-во вызовов рекурсии - 8
def matrix_multiply_intermediate(a, b):
    # в целях избежания проблем с психологическим здоровьем кода не будет
    pass


# алгоритм Штрассена - O(N^2.8)
# к-во вызовов рекурсии - 7
def strassen(a, b):
    # в целях избежания проблем с психологическим здоровьем кода не будет
    pass


def matrix_to_str(a):
    s = ""
    for row in a:
        for x in row:
            s += str(x) + " "
        s += "\n"
    return s[:-1]
