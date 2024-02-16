def get_lis_path(tail, prev, k):
    result = [-1] * k
    i = tail[k - 1]
    j = k - 1
    while i >= 0 and j >= 0:
        result[j] = i
        j -= 1
        i = prev[i]
    return result
