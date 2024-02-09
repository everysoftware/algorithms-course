
# сортировка выбором - O(N^2)
# находим минимум, ставим его первым, находим 2-й минимум
# ставим его вторым и т. д.
def selection_sort(a):
    n = len(a)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
    return a
