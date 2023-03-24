# O(1.618^N)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# мемоизация/ленивое вычисление/ДП сверху вниз - O(N^2)
def fib_td(k):
    f = [-1] * (k + 1)

    def fib_td_help(n):
        if f[n] == -1:
            if n <= 1:
                f[n] = n
            else:
                f[n] = fib_td_help(n - 1) + fib_td_help(n - 2)
        return f[n]

    return fib_td_help(k)


# ДП вперёд - O(N^2)
def fib_bu(n):
    f = [0] * (n + 2)
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


# Улучшенная по памяти версия
def fib_bu_improved(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for i in range(n - 1):
        temp = prev + curr
        prev = curr
        curr = temp
    return curr
