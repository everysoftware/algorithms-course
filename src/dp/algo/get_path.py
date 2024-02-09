
def get_lis_path(tail, prev, k):
    result = [-1] * k
    i = tail[k - 1]
    j = k - 1
    while i >= 0 and j >= 0:
        result[j] = i
        j -= 1
        i = prev[i]
    return result


# O (N + M)
def get_editing_path(a, b, d):
    n, m = len(a), len(b)
    i, j = n - 1, m - 1
    result = []
    while i >= 0 and j >= 0:
        if i > 0 and d[i][j] == d[i - 1][j] + 1:
            result.append([0, i - 1, j])
            i -= 1
        elif j > 0 and d[i][j] == d[i][j - 1] + 1:
            result.append([1, i, j])
            j -= 1
        else:
            if i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + 1:
                result.append([2, i, j])
            i -= 1
            j -= 1
    return result[::-1]
