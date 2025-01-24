# O(n)
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * (n + 1)
    # Считаем префиксные произведения
    for i in range(n):
        res[i + 1] = res[i] * nums[i]
    # Текущий суффикс.
    suffix = 1
    # Считаем произведения без элемента.
    for i in range(n - 1, -1, -1):
        # Произведение без элемента - произведение префикса на произведение суффикса.
        res[i] *= suffix
        # Обновляем суффикс.
        suffix *= nums[i]
    return res[:-1]
