from bisect import bisect_left


# O(n^2)
def lis_naive(a: list[int]) -> int:
    n = len(a)
    length = [1] * n
    # Перебираем элементы.
    for i in range(n):
        # Перебираем кандидатов, чтобы продолжить подпоследовательность.
        for j in range(i):
            # Если i элемент может продолжить подпоследовательность
            if a[j] < a[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
    return max(length)


# O(n log n)
def lis_bisect(a: list[int]) -> int:
    # tail[i] - последний элемент НВП длины i
    tail: list[int] = []
    # Перебираем элементы
    for x in a:
        # Если текущий элемент больше последнего элемента НВП, то он может её продолжить
        if not tail or x > tail[-1]:
            # Текущий элемент становится новым последним элементом НВП
            tail.append(x)
        # Если текущий элемент меньше или равен последнему элементу НВП, то он может её улучшить
        else:
            # Меньший элемент должен быть вставлен в НВП, чтобы она была как можно длиннее.
            # Например, a = [0, 7, 1, 6, 2]. Когда мы встречаем 1, то 1 должен заменить 7, чтобы НВП была
            # длиннее, так как элементов превосходящих 1 очевидно больше, чем элементов превосходящих 7.
            idx_to_insert = bisect_left(tail, x)
            # Заменяем найденный элемент НВП на текущий элемент.
            tail[idx_to_insert] = x
    return len(tail)
