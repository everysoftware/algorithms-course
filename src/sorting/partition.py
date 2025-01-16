# O(N)
def partition2(a: list[int], low: int = 0, high: int | None = None) -> int:
    # Все элементы, меньшие или равные опорному, перемещаются влево.
    high = high if high is not None else len(a) - 1
    pivot = a[low]
    j = low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j


# O(N)
def partition3(
    a: list[int], low: int = 0, high: int | None = None
) -> tuple[int, int]:
    # Если элемент меньше опорного, он перемещается влево.
    # Если больше опорного — вправо.
    # Если равен опорному, оставляется на месте.
    high = high if high is not None else len(a) - 1
    pivot = a[low]
    i = low + 1
    while i <= high:
        if a[i] < pivot:
            a[i], a[low] = a[low], a[i]
            low += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[high] = a[high], a[i]
            high -= 1
        else:
            i += 1
    return low, high
