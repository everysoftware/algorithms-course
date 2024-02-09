
# цифровая сортировка (digit sort/radix sort) - O(D*N), D - макс. число разрядов
def digit_sort(a):
    x_max = max(a) if a else 0
    d = 0
    while x_max > 0:
        d += 1
        x_max //= 10
    a_sorted = a
    p = 1
    for i in range(d):
        a_sorted = count_sort_key(a_sorted, 9, key=lambda x: (x // p) % 10)
        p *= 10
    return a_sorted
