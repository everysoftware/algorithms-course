# O(n)
def can_transform(a: str, b: str) -> bool:
    n, m = len(a), len(b)
    i, j = 0, 0
    diff_count = 0
    while i < n and j < m:
        if a[i] != b[j]:
            diff_count += 1
            if diff_count > 1:
                return False
            if n < m:
                j += 1
            elif n > m:
                i += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    if i < n or j < m:
        diff_count += 1
    return diff_count <= 1
