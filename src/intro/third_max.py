MINUS_INF = -(10**20)


# O(n)
def first_max(nums: list[int]) -> int:
    mx = MINUS_INF
    for num in nums:
        if num > mx:
            mx = num
    return mx


# O(n)
def second_max(nums: list[int]) -> int:
    mx = MINUS_INF
    mx2 = MINUS_INF
    for num in nums:
        if num > mx:
            mx2 = mx
            mx = num
        elif mx > num > mx2:
            mx2 = num
    return mx2 if mx2 != MINUS_INF else mx


# O(n)
def third_max(nums: list[int]) -> int:
    mx = MINUS_INF
    mx2 = MINUS_INF
    mx3 = MINUS_INF
    for num in nums:
        if num > mx:
            mx3 = mx2
            mx2 = mx
            mx = num
        elif mx > num > mx2:
            mx3 = mx2
            mx2 = num
        elif mx2 > num > mx3:
            mx3 = num
    return mx3 if mx3 != MINUS_INF else mx
