"""
Кодирование Хаффмана.
"""


def is_prefix_code(tree: dict[str, str]) -> bool:
    """Проверяет, является ли дерево Хаффмана префиксным кодом. Сложность: O(N^2)."""
    codes = list(tree.values())

    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            # Если один код является префиксом другого, то это не префиксный код.
            if codes[i].startswith(codes[j]) or codes[j].startswith(codes[i]):
                return False

    return True


def extract_min(queue: list[tuple[str, int]]) -> tuple[str, int]:
    """Извлекает минимальный элемент из очереди. Сложность: O(N)."""
    idx = 0
    mn = queue[0][1]

    for i, x in enumerate(queue):
        if mn > x[1]:
            mn = x[1]
            idx = i

    return queue.pop(idx)


def get_freq(string: str) -> dict[str, int]:
    """Подсчитывает частоту символов в строке. Сложность: O(N)."""
    freq = {}

    for c in string:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    return freq


"""
В данном коде обновление предков происходит на каждой итерации цикла while. 
На каждой итерации мы обрабатываем все символы в left_node[0] и right_node[0], 
которые являются строками, содержащими символы текущего узла дерева Хаффмана.

Однако, важно отметить, что каждый символ обрабатывается только один раз в процессе построения дерева 
Хаффмана. То есть, хотя на каждой итерации мы обрабатываем все символы в left_node[0] и right_node[0], 
общее количество обработанных символов на протяжении всего алгоритма ограничено O(N), 
где N - это общее количество символов во входной строке.

Таким образом, хотя каждая операция обновления предков может занимать время O(N) на каждой итерации, 
общее количество таких операций на протяжении всего алгоритма ограничено O(N), что делает общую сложность
алгоритма O(N^2). Это следует из того, что функция extract_min вызывается дважды на каждой итерации,
и каждый вызов занимает время O(N), поскольку она проходит по всем элементам в очереди для поиска
минимального элемента.
"""


def huffman_tree(string: str) -> dict[str, str]:
    """Строит дерево Хаффмана. Сложность: O(N^2)."""
    freq = get_freq(string)
    queue = list(freq.items())
    tree = {c: "" for c in freq}

    if len(freq) == 1:
        tree[string[0]] = "0"
        return tree

    while len(queue) > 1:
        # Извлекаем два узла с минимальной частотой.
        left = extract_min(queue)
        right = extract_min(queue)
        # Добавляем новый узел в очередь.
        queue.append((left[0] + right[0], left[1] + right[1]))

        # Обновляем предков.
        for ancestor in left[0]:
            tree[ancestor] = "0" + tree[ancestor]

        for ancestor in right[0]:
            tree[ancestor] = "1" + tree[ancestor]

    return tree


def huffman_encode(string: str, tree: dict[str, str]) -> str:
    """Кодирует строку с помощью дерева Хаффмана. Сложность: O(N)."""
    result = ""

    for c in string:
        result += tree[c]

    return result


def huffman_decode(string: str, tree: dict[str, str]) -> str:
    """Декодирует строку с помощью таблицы Хаффмана. Сложность: O(N)."""
    result = ""
    code = ""

    for c in string:
        code += c

        if code in tree:
            result += tree[code]
            code = ""

    return result
