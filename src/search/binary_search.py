import bisect


# O(log(N))
def binary_search(a: list[int], target: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        # m = (start + end) // 2
        m = low + (high - low) // 2
        # Если target больше, игнорируем левую половину
        if a[m] < target:
            low = m + 1
        # Если target меньше, игнорируем правую половину
        elif a[m] > target:
            high = m - 1
        # Если target равен середине, возвращаем его индекс
        else:
            return m
    return -1


# O(log(i)), i - index of target
def exp_search(a: list[int], target: int) -> int:
    n = len(a)
    end = 1
    while end < n and a[end] <= target:
        end *= 2
    end = min(end, n - 1)
    i = bisect.bisect_left(a, target, end // 2, end)
    return i if a[i] == target else -1
