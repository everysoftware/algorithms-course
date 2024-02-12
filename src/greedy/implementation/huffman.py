"""
Кодирование Хаффмана. Сложность: O(N^2).
"""


def extract_min(q: list) -> tuple:
    idx = 0
    mn = q[0][1]
    for i, x in enumerate(q):
        if mn > x[1]:
            mn = x[1]
            idx = i
    return q.pop(idx)


def huffman_tree(s: str) -> dict:
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    q = list(d.items())
    tree = {s[0]: "0"} if len(q) == 1 else {}
    while len(q) > 1:
        # Слева минимум.
        left_node = extract_min(q)
        # Справа максимум.
        right_node = extract_min(q)
        q.append((left_node[0] + right_node[0], left_node[1] + right_node[1]))
        # Обновляем предков.
        for c in left_node[0]:
            tree[c] = "0" + (tree[c] if c in tree else "")
        for c in right_node[0]:
            tree[c] = "1" + (tree[c] if c in tree else "")
    return tree


def huffman_encode(s: str, tree: dict) -> str:
    result = ""
    for c in s:
        result += tree[c]
    return result


def huffman_decode(s: str, table: dict) -> str:
    result = ""
    code = ""
    for c in s:
        code += c
        if code in table:
            result += table[code]
            code = ""
    return result
