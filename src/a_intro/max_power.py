# O(n)
def max_power(s: str) -> int:
    mx = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1
        mx = max(mx, count)
    return mx
