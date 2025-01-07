# O(N)
def partition2(a: list[int], low: int = 0, high: int | None = None) -> int:
    high = high if high is not None else len(a) - 1
    pivot = a[low]
    # Индекс, до которого отсортированы элементы
    j = low
    # Проходим по всем элементам массива
    for i in range(low + 1, high + 1):
        # Если текущий элемент меньше опорного, меняем их местами
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    a[low], a[j] = a[j], a[low]
    return j


# O(N)
def partition3(
    a: list[int], left: int = 0, right: int | None = None
) -> tuple[int, int]:
    left = left if left is not None else 0
    right = right if right is not None else len(a) - 1
    pivot = a[left]

    i = left + 1
    while i <= right:
        # Если текущий элемент меньше опорного, меняем их местами
        if a[i] < pivot:
            a[i], a[left] = a[left], a[i]
            left += 1
            i += 1

        # Если текущий элемент больше опорного, меняем его с правым элементом
        elif a[i] > pivot:
            a[i], a[right] = a[right], a[i]
            right -= 1

        # Если текущий элемент равен опорному, просто переходим к следующему элементу
        else:
            i += 1

    return left, right
