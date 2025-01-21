# O(log(N))
def lower_bound(
    a: list[int],
    target: int,
) -> int:
    """
    Находит первое вхождение элемента в отсортированной последовательности. В случае отсутствия элемента возвращает
    индекс, куда его нужно вставить, чтобы сохранить упорядоченность.

    lower_bound([3, 5, 6, 6, 6, 7], 6) -> 2
    lower_bound([3, 5, 6, 6, 6, 7], 4) -> 1
    """
    low, high = 0, len(a) - 1
    while low <= high:
        m = (low + high) // 2
        if a[m] >= target:
            high = m - 1
        else:
            low = m + 1
    return low


# O(log(N))
def upper_bound(
    a: list[int],
    target: int,
) -> int:
    """
    Находит индекс в отсортированной последовательности, куда нужно вставить элемент, чтобы сохранить упорядоченность.

    upper_bound([3, 5, 6, 6, 6, 7], 6) -> 5
    upper_bound([3, 5, 6, 6, 6, 7], 4) -> 1
    """
    low, high = 0, len(a) - 1
    while low <= high:
        m = (low + high) // 2
        if a[m] > target:
            high = m - 1
        else:
            low = m + 1
    return low


def search_range(a: list[int], target: int) -> list[int]:
    low, high = lower_bound(a, target), upper_bound(a, target) - 1
    if low < 0 or low >= len(a) or a[low] != target:
        low = -1
    if high < 0 or high >= len(a) or a[high] != target:
        high = -1
    return [low, high]
