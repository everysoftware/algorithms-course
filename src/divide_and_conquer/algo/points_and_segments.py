from src.sortings.sorting import quick_sort3


# сколько элементов меньших или равных x - O(logN)
def binary_count(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        m = (start + end) // 2
        if a[m] > x:
            end = m - 1
        else:
            start = m + 1
    return start


# Решение в среднем за
# O(NlogN) + O(NlogN) + M * O(2 * logN) = O(NlogN + MlogN) = O((N + M)logN)
def points_and_segments(segments, points):
    a, b = [], []
    for segment in segments:
        a.append(segment[0])
        b.append(segment[1])
    quick_sort3(a, 0, len(a) - 1)
    quick_sort3(b, 0, len(a) - 1)
    result = []
    for point in points:
        x = binary_count(a, point)  # сколько x >= point
        y = binary_count(b, point - 1)  # сколько x > point
        result.append(x - y)
    return result

