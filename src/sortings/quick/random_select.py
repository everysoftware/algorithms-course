
# поиск k-й порядковой статистики (a'[k]) - O(N) в среднем
def random_select(a, left, right, k):
    if left >= right:
        return a[left]
    m = random.randint(left, right)
    x = a[m]
    a[left], a[m] = a[m], a[left]
    lower, upper = partition3(a, left, right)
    if left <= k < lower:
        return random_select(a, left, lower - 1, k)
    elif lower <= k <= upper:
        return x
    else:
        return random_select(a, upper + 1, right, k)
