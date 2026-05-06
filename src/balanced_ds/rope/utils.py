def naive_rope(s: str, i: int, j: int, k: int) -> str:
    """Перемещение подстроки s[i:j + 1] на позицию k оставшейся строки"""
    without_sub = s[:i] + s[j + 1 :]
    before = without_sub[:k]
    sub = s[i : j + 1]
    after = without_sub[k:]

    return before + sub + after
