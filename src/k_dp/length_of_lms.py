# O(n^2)
def lms(a: list[int]) -> int:
    n = len(a)
    length = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] % a[j] == 0 and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
    return max(length)
