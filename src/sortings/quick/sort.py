
# быстрая сортировка - O(NlogN) в ср., O(N^2) в худш.
# называется "быстрой" потому что она реально быстрая
# на практике быстрее merge_sort, несмотря на O(N^2) в худш. случае
# разбиение массива на две части: до опорного и после - O(N)
def partition(a, left, right):
    # в качестве опорного возьмём первый
    x = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[left], a[j] = a[j], a[left]
    return j


def quick_sort(a, left, right):
    if left < right:
        m = partition(a, left, right)
        quick_sort(a, left, m - 1)
        quick_sort(a, m + 1, right)
    return a


def partition3(a, left, right):
    # в качестве опорного возьмём первый
    x = a[left]
    i = left + 1
    lower = left
    upper = right
    while i <= upper:
        if a[i] < x:
            a[i], a[lower] = a[lower], a[i]
            lower += 1
            i += 1
        elif a[i] > x:
            a[i], a[upper] = a[upper], a[i]
            upper -= 1
        else:
            i += 1
    return lower, upper


def quick_sort3(a, left, right):
    if left < right:
        k = (left + right) // 2
        a[left], a[k] = a[k], a[left]
        lower, upper = partition3(a, left, right)
        quick_sort3(a, left, lower - 1)
        quick_sort3(a, upper + 1, right)
    return a
