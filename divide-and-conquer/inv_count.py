from collections import deque


def merge_inv_count(a, b):
    result = []
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    inv_count = 0
    while i < n or j < m:
        if j == m or i < n and a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            if i < n:
                inv_count += n - i
            j += 1
    return result, inv_count


def min_power_of_2(x):
    p = 1
    while p < x:
        p *= 2
    return p


# из-за Time limit exceeded пришлось заменить list на настоящую очередь
def inverse_count(a):
    q = deque()
    n = len(a)
    # добиваем кол-во элементов до степени двойки,
    # так как итеративная сортировка слиянием рушит порядок слияния
    # из-за чего выходит неправильное число инверсий
    n1 = min_power_of_2(n)
    for i in range(n1 - n):
        q.append([0])
    for i in range(n):
        q.append([a[i]])
    count = 0
    while len(q) > 1:
        merged, inv_count = merge_inv_count(q.popleft(), q.popleft())
        q.append(merged)
        count += inv_count
    return count
