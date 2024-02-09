
# Сортировка вставками - O(N^2)
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        # ставим элемент на его место
        while j > 0 and a[j] < a[j - 1]:
            temp = a[j]
            a[j] = a[j - 1]
            a[j - 1] = temp
            j -= 1
    return a