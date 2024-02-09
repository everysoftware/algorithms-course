
# наибольшая последовательно кратная под-пть
def lss_length(a):
    n = len(a)
    if n <= 1:
        return [] if n == 0 else [0]
    d = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)
