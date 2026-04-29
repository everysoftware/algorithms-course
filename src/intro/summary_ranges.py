# O(n)
def summary_ranges(nums: list[int]) -> list[str]:
    ranges: list[list[int]] = []
    for num in nums:
        # Если список пуст или текущий элемент не продолжает последний диапазон.
        if not ranges or ranges[-1][1] + 1 != num:
            # Добавляем новый диапазон.
            ranges.append([num, num])
        # Если текущий элемент продолжает последний диапазон.
        else:
            # Обновляем конец последнего диапазона.
            ranges[-1][1] = num
    return [f"{start}->{end}" if start != end else str(start) for start, end in ranges]
