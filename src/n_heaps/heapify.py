def sift_down(a: list[int], size: int, i: int) -> list[tuple[int, int]]:
    swaps: list[tuple[int, int]] = []
    while 2 * i + 1 < size:
        left = 2 * i + 1
        right = 2 * i + 2
        j = left
        if right < size and a[right] < a[left]:
            j = right
        if a[i] <= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        swaps.append((i, j))
        i = j
    return swaps


def heapify(size: int, a: list[int]) -> list[tuple[int, int]]:
    swaps: list[tuple[int, int]] = []
    for i in range(size // 2, -1, -1):
        swaps += sift_down(a, size, i)
    return swaps
