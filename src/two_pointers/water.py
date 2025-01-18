"""
The two-pointer technique starts with one pointer at the beginning and the other at the end of the height array.
The area is calculated by taking the minimum of the two heights multiplied by the distance between them.

We then update the result if the current area is greater than the previously recorded maximum area. Next, we move the
pointer that points to the smaller height inward because moving the larger height would not increase the area.
This process continues until the two pointers meet.
"""


# O(n)
def max_area(height: list[int]) -> int:
    low, high = 0, len(height) - 1
    ans = 0
    while low < high:
        area = (high - low) * min(height[low], height[high])
        ans = max(ans, area)
        if height[low] < height[high]:
            low += 1
        else:
            high -= 1
    return ans
