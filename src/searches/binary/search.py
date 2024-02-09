def binary_search(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        m = (start + end) // 2
        if a[m] == x:
            return m
        elif a[m] > x:
            end = m - 1
        else:
            start = m + 1
    return end
