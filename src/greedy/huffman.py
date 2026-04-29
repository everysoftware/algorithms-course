"""
Визуализация:

s = "aaaaaabbcccddddeeeee"

Считаем частоту встречаемости каждого символа в строке:
freq = {a: 6, b: 2, c: 3, d: 4, e: 5}

Создаем очередь:
queue = [(a, 6), (b, 2), (c, 3), (d, 4), (e, 5)]

Объединяем два узла с минимальной частотой, пока не останется один узел:
queue = [(a, 6), (d, 4), (e, 5), (bc, 5)]
queue = [(a, 6), (bc, 5), (de, 9)]
queue = [(abc, 11), (de, 9)]
queue = [(abcde, 20)]

Дерево:

    abcde
    /    |
   de    abc
  /  |   /  |
 d   e  bc  a
        / |
       b   c

Коды:
a -> 11
b -> 100
c -> 101
d -> 00
e -> 01

encoded = "111111111111100100101101101000000000101010101"
"""


# O(n)
def huffman_encode(s: str) -> tuple[str, dict[str, str]]:
    result = ""
    tree = huffman_tree(s)
    for c in s:
        result += tree[c]
    return result, tree


# O(n)
def huffman_decode(s: str, tree: dict[str, str]) -> str:
    result = ""
    code = ""
    for c in s:
        code += c
        if code in tree:
            result += tree[code]
            code = ""
    return result


# O(n^2)
def huffman_tree(s: str) -> dict[str, str]:
    # Считаем частоту встречаемости каждого символа в строке.
    freq = count_chars(s)
    # Создаем очередь: каждый элемент очереди представляет собой кортеж (символ, частота).
    queue = list(freq.items())
    # Создаем словарь для хранения кодов Хаффмана.
    tree = {c: "" for c in freq}
    # Если в строке есть только один символ, то кодируем его как "0".
    if len(freq) == 1:
        tree[s[0]] = "0"
    # Пока в очереди есть хотя бы два узла.
    while len(queue) >= 2:
        # Извлекаем два узла с минимальной частотой - их нужно закодировать в первую очередь.
        left = extract_min(queue)
        right = extract_min(queue)
        # Добавляем новый узел в очередь:
        # его название равно конкатенации названий двух извлеченных узлов (a + b = ab),
        # а его частота равна сумме частот двух извлеченных узлов (1 + 2 = 3).
        queue.append((left[0] + right[0], left[1] + right[1]))
        # Обновляем предков: добавляем "0" к коду левого узла и "1" к коду правого узла.
        for ancestor in left[0]:
            tree[ancestor] = "0" + tree[ancestor]
        for ancestor in right[0]:
            tree[ancestor] = "1" + tree[ancestor]
    return tree


# O(n)
def count_chars(s: str) -> dict[str, int]:
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq


# O(n)
def extract_min(queue: list[tuple[str, int]]) -> tuple[str, int]:
    idx = 0
    mn = queue[0][1]
    for i, x in enumerate(queue):
        if mn > x[1]:
            mn = x[1]
            idx = i
    return queue.pop(idx)
