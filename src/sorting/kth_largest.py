from .partition import partition3


# O(n) в среднем, O(n^2) в худшем
def kth_largest(nums: list[int], k: int) -> int:
    return quick_select(nums, len(nums) - k + 1)


def quick_select(a: list[int], k: int) -> int:
    if len(a) == 1:
        return a[0]
    k -= 1
    low = 0
    high = len(a) - 1
    while True:
        left_idx, right_idx = partition3(a, low, high)
        if left_idx <= k <= right_idx:
            return a[k]
        elif k < left_idx:
            high = left_idx - 1
        else:
            low = right_idx + 1
