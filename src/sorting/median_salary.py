from .kth_largest import quick_select


# O(N) in average, O(N^2) the worst
def median_salary(scores: list[int]) -> float:
    n = len(scores)
    if n % 2 == 1:
        # If the number of elements is odd, return the middle element
        return quick_select(scores, n // 2 + 1)
    else:
        # If the number of elements is even, return the average of the two middle elements
        left = quick_select(scores, n // 2)
        right = quick_select(scores, n // 2 + 1)
        median = (left + right) / 2
        return round(median, 6)
