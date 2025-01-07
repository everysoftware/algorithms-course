from typing import Callable


# O(N + M)
def counting_sort(
    a: list[int], m: int, *, key: Callable[[int], int] | None = None
) -> list[int]:
    n = len(a)
    keys = a if key is None else list(map(key, a))
    # freq[i] - сколько раз встречается i
    freq = [0] * (m + 1)

    for i in range(n):
        freq[keys[i]] += 1

    result = []
    for i, count in enumerate(freq):
        result.extend([i] * count)

    return result
