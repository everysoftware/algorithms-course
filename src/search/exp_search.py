from .binary_search import local_binary_search


# O(log(i)), i - index of target
def exp_search(a: list[int], target: int) -> int:
    n = len(a)
    end = 1
    while end < n and a[end] <= target:
        end *= 2
    end = min(end, n - 1)
    i = local_binary_search(a, target, end // 2, end)
    return i
