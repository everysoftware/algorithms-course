# O(n^2)
def two_sum_naive(arr: list[int], target: int) -> tuple[int, int]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return i, j
    return -1, -1


# O(n)
def two_sum_tp(arr: list[int], target: int) -> tuple[int, int]:
    n = len(arr)
    low, high = 0, n - 1
    while low < high:
        current_sum = arr[low] + arr[high]
        if current_sum == target:
            return low, high
        elif current_sum < target:
            low += 1
        else:
            high -= 1
    return -1, -1
