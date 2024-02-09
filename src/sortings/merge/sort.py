
#  Сортировка слиянием - O(NlogN)

# O(N + M)
# процедура слияния - первым элементом резульютирующего
# массива будет меньший из первых элементов данных массивов.
# остальные эл-ты заполняются аналогично
def merge(a, b):
    result = []
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    while i < n or j < m:
        if j == m or i < n and a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result


def merge_sort(a, left, right):
    if left < right:
        m = (left + right) // 2
        # производим сливание двух отсортированных кусков
        left_part = merge_sort(a, left, m)
        right_part = merge_sort(a, m + 1, right)
        return merge(left_part, right_part)
    # дошли до того, что сортируем одноэлементный (или пустой) массив
    else:
        return [a[left]] if len(a) > 0 else []


# реализация сортировки слиянием без рекурсии
def iterative_merge_sort(a):
    q = []
    n = len(a)
    for i in range(n):
        q.append([a[i]])
    while len(q) > 1:
        q.append(merge(q.pop(0), q.pop(0)))
    return q.pop(0) if len(q) > 0 else []