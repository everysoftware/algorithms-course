
# Наибольшая невозрастающая подпоследовательность
def lnis(a):
    n = len(a)
    if n <= 1:
        return [] if n == 0 else [0]
    tail = [0] * n
    prev = [-1] * n
    tail[0] = 0
    k = 1
    for i in range(1, n):
        if a[i] <= a[tail[k - 1]]:
            prev[i] = tail[k - 1]
            tail[k] = i
            k += 1
        else:
            # находим индекс элемента, который строго меньше нашего
            # a[m] > x - так мы ищем строго больше
            # добавляем минусы, происходит магия:
            # -a[m] > -x <=> a[m] < x
            idx = upper_bound(tail, -a[i], 0, k - 1, key=lambda x: -a[x])
            prev[i] = tail[idx - 1]
            tail[idx] = i
    return get_path(tail, prev, k)

