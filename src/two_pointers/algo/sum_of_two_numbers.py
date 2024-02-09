def sum_of_two_numbers_naive(arr: list[int], target: int) -> tuple[int, int]:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

    return -1, -1


def sum_of_two_numbers(arr: list[int], target: int) -> list[int]:
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return -1, -1
